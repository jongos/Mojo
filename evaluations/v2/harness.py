"""Prepare isolated condition packets and check retained evaluation artifacts.

This tool does not call a model or assign writing-quality scores.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def input_paths():
    return [ROOT / 'cases.json', ROOT / 'rubric.json',
            *sorted((ROOT / 'conditions').rglob('*.md')),
            *sorted((ROOT / 'packets').glob('*.json'))]


def text_hash(path):
    # Portable across Git LF and Windows CRLF checkouts.
    return hashlib.sha256(path.read_text(encoding='utf-8').encode('utf-8')).hexdigest()


def cases():
    data = read(ROOT / 'cases.json')
    ids = [c['id'] for c in data]
    assert len(data) == 60 and len(set(ids)) == 60, 'Expected 60 unique cases'
    families = {c['family'] for c in data}
    assert len(families) == 6, 'Expected six families'
    for family in families:
        group = [c for c in data if c['family'] == family]
        assert len(group) == 10
        assert sum(c['split'] == 'development' for c in group) == 5
        assert sum(c['split'] == 'heldout' for c in group) == 5
        assert sum(c['pilot'] is True for c in group) == 2
    assert all(c['split'] == 'development' for c in data if c['pilot'])
    rubric = read(ROOT / 'rubric.json')
    assert set(rubric) == set(ids)
    for row in rubric.values():
        assert row['invariants'] and row['questions'] and row['hard_failures']
        assert isinstance(row['protected'], list)
    return data


def prepare():
    if (ROOT / 'input-hashes.json').exists():
        verify_hashes()
    data = cases()
    instructions = {
        'baseline': '',
        'generic': 'Write clearly and concisely. Preserve facts and the requested voice.',
    }
    for name in ['current', 'candidate']:
        folder = ROOT / 'conditions' / name
        instructions[name] = '\n\n'.join(
            f'### {p.relative_to(folder).as_posix()}\n{p.read_text(encoding="utf-8")}'
            for p in [folder / 'SKILL.md', *sorted((folder / 'references').glob('*.md'))]
        )
    for condition, instruction in instructions.items():
        for phase in ['pilot', 'remaining']:
            selected = [c for c in data if c['pilot'] == (phase == 'pilot')]
            write(ROOT / 'packets' / f'{condition}-{phase}.json', {
                'instructions': instruction,
                'tasks': [{'id': c['id'], 'request': c['request']} for c in selected],
            })
    # Freeze inputs, not results. Adding observations never rewrites the protocol.
    write(ROOT / 'input-hashes.json', {
        p.relative_to(ROOT).as_posix(): text_hash(p)
        for p in input_paths()
    })


def check_outputs(path, phase):
    data = cases()
    expected = {c['id'] for c in data if phase == 'all' or c['pilot'] == (phase == 'pilot')}
    outputs = read(path)
    ids = [o['id'] for o in outputs]
    assert len(ids) == len(set(ids)) and set(ids) == expected, 'Missing, extra or duplicate outputs'
    assert all(isinstance(o['output'], str) and o['output'].strip() for o in outputs)
    rubric = read(ROOT / 'rubric.json')
    flags = []
    for row in outputs:
        missing = [s for s in rubric[row['id']]['protected'] if s not in row['output']]
        if missing:
            flags.append({'id': row['id'], 'missing_protected': missing})
    return {'outputs': len(outputs), 'protected_span_flags': flags,
            'scope': 'Completeness and exact spans only; semantic review is separate.'}


def verify_hashes():
    inventory = read(ROOT / 'input-hashes.json')
    assert set(inventory) == {p.relative_to(ROOT).as_posix() for p in input_paths()}, 'Frozen input file set changed'
    for name, expected in inventory.items():
        assert text_hash(ROOT / name) == expected, name


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'check', 'verify'])
    parser.add_argument('--outputs', type=Path)
    parser.add_argument('--phase', choices=['pilot', 'remaining', 'all'], default='all')
    args = parser.parse_args()
    if args.command == 'prepare':
        prepare()
        print('Prepared four conditions, 12 pilot cases and 48 remaining cases; froze inputs.')
    elif args.command == 'verify':
        cases(); verify_hashes(); print('Benchmark structure and frozen inputs passed.')
    else:
        if args.outputs is None:
            parser.error('--outputs is required for check')
        print(json.dumps(check_outputs(args.outputs, args.phase), ensure_ascii=False, indent=2))
