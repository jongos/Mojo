"""Validate retained judgments and report descriptive results, without grading prose."""
from collections import Counter
from harness import ROOT, read, write, verify_hashes, check_outputs, cases

DIMENSIONS = {'meaning', 'usefulness', 'clarity', 'voice_scope', 'edit_restraint'}


def summarize(path, mapping):
    rows = read(path)
    ids = [row['id'] for row in rows]
    assert len(ids) == len(set(ids)), 'Duplicate judged case'
    totals = {name: {'cases': 0, 'score_totals': Counter(), 'preferred': 0,
                     'comprehension_passes': 0, 'hard_failures': []}
              for name in ['baseline', 'generic', 'current', 'candidate']}
    for row in rows:
        labels = [a['label'] for a in row['assessments']]
        assert len(labels) == 4 and set(labels) == set('ABCD')
        assert row['preferred'] and set(row['preferred']) <= set(labels)
        for assessment in row['assessments']:
            scores = assessment['scores']
            assert set(scores) == DIMENSIONS
            assert all(type(v) is int and 0 <= v <= 2 for v in scores.values())
            assert type(assessment['comprehension_pass']) is bool
            assert isinstance(assessment['hard_failures'], list)
            condition = mapping[row['id']][assessment['label']]
            result = totals[condition]
            result['cases'] += 1
            result['score_totals'].update(scores)
            result['preferred'] += assessment['label'] in row['preferred']
            result['comprehension_passes'] += assessment['comprehension_pass']
            if assessment['hard_failures']:
                result['hard_failures'].append({'id': row['id'], 'failures': assessment['hard_failures']})
    return {'case_ids': ids, 'conditions': totals}


def main():
    verify_hashes()
    results = {'reviews': {}, 'output_checks': {}}
    corpus = cases()
    pilot_ids = [c['id'] for c in corpus if c['pilot']]
    remaining_ids = [c['id'] for c in corpus if not c['pilot']]
    expected = {'pilot.json': pilot_ids, 'pilot-reversed.json': pilot_ids,
                'remaining-a.json': remaining_ids[:24], 'remaining-b.json': remaining_ids[24:],
                'remaining-sample-reversed.json': [i for i in remaining_ids if i[1:] in ['06', '10']]}
    for phase in ['pilot', 'remaining']:
        mapping_path = ROOT / 'condition-maps' / f'{phase}.json'
        if not mapping_path.exists():
            continue
        mapping = read(mapping_path)
        for name in ['baseline', 'generic', 'current', 'candidate']:
            output = ROOT / 'outputs' / f'{name}-{phase}.json'
            if output.exists():
                results['output_checks'][output.name] = check_outputs(output, phase)
        for path in sorted((ROOT / 'judgments').glob(f'{phase}*.json')):
            assert path.name in expected, f'Unexpected judgment file: {path.name}'
            result = summarize(path, mapping)
            assert set(result['case_ids']) == set(expected[path.name]), f'Incomplete review: {path.name}'
            results['reviews'][path.name] = result
    results['complete_primary_and_reversed_review'] = set(results['reviews']) == set(expected)
    write(ROOT / 'summary.json', results)
    if results['complete_primary_and_reversed_review']:
        comparison = {}
        for group, files in {
            'primary': ['pilot.json', 'remaining-a.json', 'remaining-b.json'],
            'reversed': ['pilot-reversed.json', 'remaining-sample-reversed.json'],
        }.items():
            comparison[group] = {}
            for name in ['baseline', 'generic', 'current', 'candidate']:
                parts = [results['reviews'][f]['conditions'][name] for f in files]
                comparison[group][name] = {
                    'cases': sum(p['cases'] for p in parts),
                    'scores': {d: sum(p['score_totals'][d] for p in parts) for d in sorted(DIMENSIONS)},
                    'preferred_or_tied': sum(p['preferred'] for p in parts),
                    'hard_failure_cases': [x['id'] for p in parts for x in p['hard_failures']],
                }
        write(ROOT / 'comparison.json', comparison)
        primary = {r['id']: r for f in ['pilot.json', 'remaining-a.json', 'remaining-b.json']
                   for r in read(ROOT / 'judgments' / f)}
        differences = []
        for f in ['pilot-reversed.json', 'remaining-sample-reversed.json']:
            for second in read(ROOT / 'judgments' / f):
                first = primary[second['id']]
                a = {x['label']: x for x in first['assessments']}
                b = {x['label']: x for x in second['assessments']}
                changed = [label for label in a if any(a[label][key] != b[label][key]
                           for key in ['scores', 'hard_failures', 'comprehension_pass'])]
                preference_changed = set(first['preferred']) != set(second['preferred'])
                if changed or preference_changed:
                    differences.append({'id': second['id'], 'assessment_labels_changed': changed,
                                        'preference_changed': preference_changed,
                                        'primary_preferred': first['preferred'],
                                        'reversed_preferred': second['preferred']})
        write(ROOT / 'review-disagreements.json', differences)
    print('Validated judgments and wrote summary.json; scores are descriptive, not a release decision.')


if __name__ == '__main__':
    main()
