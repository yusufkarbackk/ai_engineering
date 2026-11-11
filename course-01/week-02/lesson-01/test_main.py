import unittest
from unittest.mock import patch
from main import analyze_data


class TestAnalyze(unittest.TestCase):
    def test_average(self):
        result = {"average": 30.0, "maximum": 50, "minimum": 10}

        with patch.dict(result, clear=True):
            result = analyze_data([10, 20, 30, 40, 50])

        self.assertEqual(result["average"], 30.0)

    def test_maximum(self):
        result = {"average": 30.0, "maximum": 50, "minimum": 10}

        with patch.dict(result, clear=True):
            result = analyze_data([10, 20, 30, 40, 50])

        self.assertEqual(result["maximum"], 50)

    def test_minimum(self):
        result = {"average": 30.0, "maximum": 50, "minimum": 10}

        with patch.dict(result, clear=True):
            result = analyze_data([10, 20, 30, 40, 50])

        self.assertEqual(result["minimum"], 10)

    def test_analyze_data(self):
        result = {"average": 30.0, "maximum": 50, "minimum": 10}

        with patch.dict(result, clear=True):
            result = analyze_data([10, 20, 30, 40, 50])

        self.assertEqual(result, {"average": 30.0, "maximum": 50, "minimum": 10})

    def test_empty_numbers(self):
        result = {"average": 30.0, "maximum": 50, "minimum": 10}

        with patch.dict(result, clear=True):
            with self.assertRaises(ValueError):
                analyze_data([])

        # with patch.dict(result, clear=True):
        #     with self.assertLogs("main", level="ERROR") as captured:
        #         with self.assertRaises(ValueError):
        #             get_config()

        # self.assertIn("API_BASE_URL kosong", captured.output[0])

        # self.assertEqual(result, {"average": 30.0, "maximum": 50, "minimum": 10})


if __name__ == "__main__":
    unittest.main()
