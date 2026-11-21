import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FixtureTests(unittest.TestCase):
    def test_synthetic_records_match_documented_envelope(self):
        path = ROOT / 'fixtures' / 'records.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(data['dataset'], 'help')
        self.assertIsInstance(data['records'], list)
        self.assertGreaterEqual(len(data['records']), 3)
        identifiers = [row['id'] for row in data['records']]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertTrue(all(isinstance(row, dict) for row in data['records']))

    def test_help_events_checks_attempts_and_future_support_share_task_versions(self):
        data = json.loads((ROOT / 'fixtures' / 'records.json').read_text(encoding='utf-8'))
        self.assertEqual({row['version'] for row in data['catalogs']['tasks']}, {'v1', 'v2'})
        kinds = {row['kind'] for row in data['records']}
        self.assertTrue({'help-event', 'learner-check', 'independent-attempt', 'support-plan'} <= kinds)
        self.assertTrue(any(row.get('status') == 'not-recorded' for row in data['records']))

if __name__ == '__main__':
    unittest.main()
