"""Verify point-in-time inclusion, missing activity and anchor grain."""
from pathlib import Path
import sqlite3
import unittest


class PointInTimeTests(unittest.TestCase):
    def test_only_available_past_events_enter_features(self) -> None:
        with sqlite3.connect(":memory:") as connection:
            connection.executescript("""
                CREATE TABLE anchors(entity_id TEXT, reference_time TEXT, observation_start TEXT,
                                     PRIMARY KEY(entity_id, reference_time));
                CREATE TABLE events(event_id INTEGER PRIMARY KEY, entity_id TEXT, event_time TEXT,
                                    available_at TEXT, amount REAL);
            """)
            connection.executemany("INSERT INTO anchors VALUES (?, ?, ?)", [
                ("a", "2026-04-01 09:00:00", "2026-03-01 00:00:00"),
                ("a", "2026-04-01 11:00:00", "2026-03-01 00:00:00"),
                ("b", "2026-04-01 09:00:00", "2026-03-01 00:00:00"),
            ])
            connection.executemany("INSERT INTO events VALUES (?, ?, ?, ?, ?)", [
                (1, "a", "2026-03-20 00:00:00", "2026-03-20 01:00:00", 10),
                (2, "a", "2026-03-31 00:00:00", "2026-04-01 10:00:00", 20),
                (3, "a", "2026-04-01 09:00:00", "2026-04-01 09:00:00", 30),
                (4, "a", "2026-02-28 00:00:00", "2026-02-28 01:00:00", 40),
            ])
            query = (Path(__file__).resolve().parents[1] / "examples/sql/point-in-time.sql").read_text(encoding="utf-8")
            rows = sorted(connection.execute(query).fetchall())
            self.assertEqual(rows, [("a", "2026-04-01 09:00:00", 1, 10),
                                    ("a", "2026-04-01 11:00:00", 3, 60),
                                    ("b", "2026-04-01 09:00:00", 0, 0)])


if __name__ == "__main__":
    unittest.main()
