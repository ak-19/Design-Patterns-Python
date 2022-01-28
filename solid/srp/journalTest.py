import unittest

from journal import Journal

class JournalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.journal = Journal()
        return super().setUp()

    def test_add_entry(self):
        self.journal.add_entry('first entry')
        self.journal.add_entry('second entry')
        self.assertEquals(self.journal.entries[0], '1 = first entry')
        self.assertEquals(self.journal.entries[1], '2 = second entry')

    def test_remove_entry(self):
        self.journal.add_entry('first entry')
        self.journal.remove_entry(0)
        self.assertEqual(len(self.journal.entries), 0)        

if __name__ == "__main__":
    unittest.main()