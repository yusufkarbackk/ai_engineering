import unittest
from main import analyze_data
import data_utils


class TestAnalyze(unittest.TestCase):
    def test_average(self):

        result = data_utils.calculate_average([10, 20, 30, 40, 50])

        self.assertEqual(result, 30.0)

    def test_maximum(self):

        result = data_utils.find_max([10, 20, 30, 40, 50])

        self.assertEqual(result, 50)

    def test_minimum(self):

        result = data_utils.find_min([10, 20, 30, 40, 50])

        self.assertEqual(result, 10)

    def test_analyze_data(self):
        result = analyze_data([10, 20, 30, 40, 50])

        self.assertEqual(result, {"average": 30.0, "maximum": 50, "minimum": 10})

    def test_empty_numbers(self):
        with self.assertRaises(ValueError):
            analyze_data([])


if __name__ == "__main__":
    unittest.main()
