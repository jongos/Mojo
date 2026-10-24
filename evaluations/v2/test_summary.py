import tempfile
import unittest
from pathlib import Path
from harness import write
from summarize import summarize, DIMENSIONS


class SummaryTests(unittest.TestCase):
    def test_labels_are_mapped_per_case_and_ties_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'review.json'
            mapping = {'x': dict(zip('ABCD', ['candidate', 'current', 'generic', 'baseline']))}
            row = {'id': 'x', 'preferred': ['A', 'B'], 'assessments': [
                {'label': label, 'scores': dict.fromkeys(DIMENSIONS, 2),
                 'hard_failures': ['changed scope'] if label == 'D' else [],
                 'comprehension_pass': label != 'D'} for label in 'ABCD']}
            write(path, [row])
            result = summarize(path, mapping)['conditions']
            self.assertEqual(result['candidate']['preferred'], 1)
            self.assertEqual(result['current']['preferred'], 1)
            self.assertEqual(result['baseline']['comprehension_passes'], 0)
            self.assertEqual(result['baseline']['hard_failures'][0]['id'], 'x')
            row['assessments'][0]['scores']['meaning'] = 3
            write(path, [row])
            with self.assertRaises(AssertionError):
                summarize(path, mapping)


if __name__ == '__main__':
    unittest.main()
