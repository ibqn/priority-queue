import unittest
from priority_queue import MaxPQ


class TestPriorityQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.pq = MaxPQ()

    def test_basic_priority_queue(self) -> None:
        self.pq.insert("B")
        self.pq.insert("L")
        self.pq.insert("E")
        self.pq.insert("K")

        self.assertEqual(4, self.pq.size())

        for key in "LKEB":
            self.assertEqual(key, self.pq.delete_max())


if __name__ == "__main__":
    unittest.main()
