"""Prepare and validate the separately retained post-benchmark revision."""
import argparse
from harness import ROOT, read, write, text_hash, cases, verify_hashes, check_outputs
from summarize import DIMENSIONS

FOLLOWUP = ROOT / 'followup'


def inventory_at(path):
    # Accept inventories authored on Windows in a POSIX checkout too.
    return {name.replace('\\', '/'): value for name, value in read(path).items()}


def verify_instructions():
    inventory = inventory_at(FOLLOWUP / 'instruction-hashes.json')
    paths = [FOLLOWUP / 'skill/SKILL.md', *sorted((FOLLOWUP / 'skill/references').glob('*.md'))]
    assert set(inventory) == {p.relative_to(FOLLOWUP).as_posix() for p in paths}
    for name, expected in inventory.items():
        assert text_hash(FOLLOWUP / name) == expected
        if FOLLOWUP.name == 'final-revision':
            live = ROOT.parent.parent / 'skills/mojo-language' / (FOLLOWUP / name).relative_to(FOLLOWUP / 'skill')
            assert text_hash(live) == expected, f'Shipped instructions differ: {live}'


def supplemental():
    data = read(FOLLOWUP / 'cases.json')
    assert len(data) == 12 and {x['id'] for x in data} == {f'T{i:02}' for i in range(1, 13)}
    rubric = read(FOLLOWUP / 'rubric.json')
    assert set(rubric) == {x['id'] for x in data}
    return data


def prepare():
    verify_instructions()
    if (FOLLOWUP / 'input-hashes.json').exists():
        verify_inputs()
    instruction = read(FOLLOWUP / 'packets/regression-pilot.json')['instructions']
    write(FOLLOWUP / 'packets/supplemental.json', {'instructions': instruction, 'tasks': supplemental()})
    paths = [FOLLOWUP / 'cases.json', FOLLOWUP / 'rubric.json', *sorted((FOLLOWUP / 'packets').glob('*.json'))]
    write(FOLLOWUP / 'input-hashes.json', {p.relative_to(FOLLOWUP).as_posix(): text_hash(p) for p in paths})


def verify_inputs():
    verify_instructions(); verify_hashes()
    paths = [FOLLOWUP / 'cases.json', FOLLOWUP / 'rubric.json', *sorted((FOLLOWUP / 'packets').glob('*.json'))]
    inventory = inventory_at(FOLLOWUP / 'input-hashes.json')
    assert set(inventory) == {p.relative_to(FOLLOWUP).as_posix() for p in paths}
    for name, expected in inventory.items():
        assert text_hash(FOLLOWUP / name) == expected


def review():
    verify_inputs()
    original = cases()
    rubric = read(ROOT / 'rubric.json')
    outputs = []
    checks = {}
    for phase in ['pilot', 'remaining']:
        path = FOLLOWUP / 'outputs' / f'regression-{phase}.json'
        checks[phase] = check_outputs(path, phase)
        outputs.extend(read(path))
    by_id = {x['id']: x['output'] for x in outputs}
    packet = [dict(id=c['id'], request=c['request'], rubric=rubric[c['id']], output=by_id[c['id']]) for c in original]
    for suffix, subset in [('a', packet[:30]), ('b', packet[30:])]:
        write(FOLLOWUP / 'review-packets' / f'regression-{suffix}.json', subset)
    data = supplemental(); rubric = read(FOLLOWUP / 'rubric.json')
    outputs = read(FOLLOWUP / 'outputs/supplemental.json')
    assert len(outputs) == 12 and {x['id'] for x in outputs} == {x['id'] for x in data}
    assert all(isinstance(x['output'], str) and x['output'].strip() for x in outputs)
    by_id = {x['id']: x['output'] for x in outputs}
    checks['supplemental'] = {'outputs': 12, 'protected_span_flags': [
        {'id': c['id'], 'missing_protected': [s for s in rubric[c['id']]['protected'] if s not in by_id[c['id']]]}
        for c in data if any(s not in by_id[c['id']] for s in rubric[c['id']]['protected'])]}
    write(FOLLOWUP / 'review-packets/supplemental.json', [dict(id=c['id'], request=c['request'], rubric=rubric[c['id']], output=by_id[c['id']]) for c in data])
    write(FOLLOWUP / 'output-checks.json', checks)


def summarize():
    verify_inputs()
    results = {}
    for name in ['regression-a', 'regression-b', 'supplemental']:
        rows = read(FOLLOWUP / 'judgments' / f'{name}.json')
        packet = read(FOLLOWUP / 'review-packets' / f'{name}.json')
        assert len(rows) == len(packet) and {r['id'] for r in rows} == {r['id'] for r in packet}
        for row in rows:
            assert set(row['scores']) == DIMENSIONS
            assert all(type(v) is int and 0 <= v <= 2 for v in row['scores'].values())
            assert isinstance(row['hard_failures'], list) and type(row['comprehension_pass']) is bool
        results[name] = {'cases': len(rows), 'scores': {d: sum(r['scores'][d] for r in rows) for d in sorted(DIMENSIONS)},
                         'comprehension_passes': sum(r['comprehension_pass'] for r in rows),
                         'hard_failures': [{'id': r['id'], 'failures': r['hard_failures']} for r in rows if r['hard_failures']]}
    write(FOLLOWUP / 'summary.json', results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'verify', 'review', 'summarize'])
    parser.add_argument('--run', choices=['followup', 'final-revision'], default='followup')
    args = parser.parse_args()
    FOLLOWUP = ROOT / args.run
    command = args.command
    {'prepare': prepare, 'verify': verify_inputs, 'review': review, 'summarize': summarize}[command]()
    print(f'Follow-up {command} passed.')
