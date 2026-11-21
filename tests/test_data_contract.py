import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'demands': ['id', 'village', 'site', 'date', 'start', 'end', 'urgency', 'verified'], 'legs': ['demand', 'leg', 'duration', 'roles', 'gap_min', 'gap_max'], 'skills': ['worker', 'skill', 'state', 'date'], 'offers': ['scenario', 'worker', 'date', 'start', 'end', 'home'], 'travel': ['origin', 'destination', 'minutes'], 'targets': ['village', 'min_tasks'], 'commitments': ['id', 'demand', 'leg', 'worker', 'role', 'start', 'end', 'accepted_at'], 'changes': ['id', 'action', 'subject', 'scope', 'at']}


class DataContractTests(unittest.TestCase):
    def test_readable_source_tables(self):
        for name, fields in FIELDS.items():
            with self.subTest(table=name):
                text = (ROOT / 'data' / (name + '.csv')).read_text(encoding='utf-8')
                with io.StringIO(text, newline='') as stream:
                    reader = csv.reader(stream, strict=True)
                    self.assertEqual(next(reader), fields)
                    rows = list(reader)
                self.assertTrue(rows)
                self.assertTrue(all(len(row) == len(fields) for row in rows))
