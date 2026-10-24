import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import harness


class HarnessTests(unittest.TestCase):
    def test_frozen_file_set_and_content(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(harness, 'ROOT', Path(temp)):
            root = Path(temp)
            for name in ['cases.json', 'rubric.json', 'conditions/current/SKILL.md']:
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                (root / name).write_text('test\n', encoding='utf-8')
            harness.write(root / 'input-hashes.json', {p.relative_to(root).as_posix():harness.text_hash(p) for p in harness.input_paths()})
            harness.verify_hashes()
            (root / 'conditions/current/extra.md').write_text('new guidance', encoding='utf-8')
            with self.assertRaisesRegex(AssertionError, 'file set'):
                harness.verify_hashes()

    def test_duplicates_missing_and_empty_outputs_rejected(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(harness, 'ROOT', Path(temp)), patch.object(harness, 'cases', return_value=[{'id':'x', 'pilot':True}]):
            root = Path(temp)
            harness.write(root / 'rubric.json', {'x':{'protected':['KEEP']}})
            for rows in [[], [{'id':'x','output':'KEEP'}, {'id':'x','output':'other'}], [{'id':'x','output':''}], [{'id':'y','output':'KEEP'}]]:
                harness.write(root / 'outputs.json', rows)
                with self.assertRaises(AssertionError):
                    harness.check_outputs(root / 'outputs.json', 'pilot')
            harness.write(root / 'outputs.json', [{'id':'x','output':'changed'}])
            self.assertEqual(harness.check_outputs(root / 'outputs.json','pilot')['protected_span_flags'][0]['missing_protected'], ['KEEP'])

    def test_text_hash_is_newline_portable(self):
        with tempfile.TemporaryDirectory() as temp:
            a, b = Path(temp)/'a', Path(temp)/'b'
            a.write_bytes(b'a\nb\n'); b.write_bytes(b'a\r\nb\r\n')
            self.assertEqual(harness.text_hash(a),harness.text_hash(b))


if __name__ == '__main__':
    unittest.main()
