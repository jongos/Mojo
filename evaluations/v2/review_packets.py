"""Anonymize retained outputs for independent, order-counterbalanced review."""
import argparse
import random
from harness import ROOT, cases, read, write, check_outputs, verify_hashes


def prepare(phase):
    verify_hashes()
    corpus = [c for c in cases() if c['pilot'] == (phase == 'pilot')]
    rubric = read(ROOT / 'rubric.json')
    names = ['baseline', 'generic', 'current', 'candidate']
    for name in names:
        check_outputs(ROOT / 'outputs' / f'{name}-{phase}.json', phase)
    outputs = {name: {o['id']: o['output'] for o in read(ROOT / 'outputs' / f'{name}-{phase}.json')} for name in names}
    rng = random.Random(20261024)
    packet, mapping = [], {}
    for case in corpus:
        shuffled = names[:]; rng.shuffle(shuffled)
        mapping[case['id']] = dict(zip('ABCD', shuffled))
        packet.append({
            'id': case['id'], 'request': case['request'], 'rubric': rubric[case['id']],
            'outputs': [{'label': label, 'output': outputs[name][case['id']]} for label, name in mapping[case['id']].items()],
        })
    write(ROOT / 'review-packets' / f'{phase}.json', packet)
    write(ROOT / 'condition-maps' / f'{phase}.json', mapping)
    # Same labels/text, reversed presentation; map stays outside reviewer packet.
    write(ROOT / 'review-packets' / f'{phase}-reversed.json', [dict(row, outputs=list(reversed(row['outputs']))) for row in packet])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=['pilot', 'remaining'])
    prepare(parser.parse_args().phase)
