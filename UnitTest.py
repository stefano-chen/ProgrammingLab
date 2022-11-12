import unittest
from sum_csv_pandas import sum_csv_pandas


class SumTest(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(sum_csv_pandas("test.csv"), 31.6)

    def test_exc(self):
        with self.assertRaises(Exception):
            sum_csv_pandas("t.csv")


if __name__ == '__main__':
    unittest.main()
