import unittest
from unittest.mock import patch
from main import get_config
import os


class TestFetchEnv(unittest.TestCase):

    def test_get_config_success(self):

        env = {
            "API_BASE_URL": "https://jsonplaceholder.typicode.com",
            "API_TIMEOUT": "3",
        }

        with patch.dict(os.environ, env, clear=True):
            with self.assertLogs("main", level="INFO") as captured:
                result = get_config()

        self.assertIn("config sukses", captured.output[0])
        self.assertEqual(result["api_timeout"], 3)

    def test_get_config_empty_base_url(self):
        env = {
            "API_BASE_URL": "",
            "API_TIMEOUT": "3",
        }

        with patch.dict(os.environ, env, clear=True):
            with self.assertLogs("main", level="ERROR") as captured:
                with self.assertRaises(ValueError):
                    get_config()

        self.assertIn("API_BASE_URL kosong", captured.output[0])

    def test_get_config_missing_base_url(self):
        env = {
            "API_TIMEOUT": "3",
        }

        with patch.dict(os.environ, env, clear=True):
            with self.assertLogs("main", level="ERROR") as captured:
                with self.assertRaises(ValueError):
                    get_config()

        self.assertIn("API_BASE_URL kosong", captured.output[0])

    def test_get_config_default_timeout(self):
        env = {
            "API_BASE_URL": "https://jsonplaceholder.typicode.com",
        }

        with patch.dict(os.environ, env, clear=True):
            with self.assertLogs("main", level="WARNING") as captured:
                result = get_config()

        self.assertIn(
            "API_TIMEOUT tidak ditemukan, menggunakan default 5", captured.output[0]
        )
        self.assertEqual(result["api_timeout"], 5)
        self.assertIsInstance(result["api_timeout"], int)

    def test_get_config_invalid_timeout(self):
        env = {
            "API_BASE_URL": "https://jsonplaceholder.typicode.com",
            "API_TIMEOUT": "abc",
        }

        with patch.dict(os.environ, env, clear=True):
            with self.assertLogs("main", level="ERROR") as captured:
                with self.assertRaises(ValueError):
                    get_config()

        self.assertIn("API_TIMEOUT invalid", captured.output[0])


if __name__ == "__main__":
    unittest.main()
