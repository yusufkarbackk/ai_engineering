import unittest
from unittest.mock import patch
from main import get_config
import os


class TestFetchEnv(unittest.TestCase):

    def test_fetch_get_success(self):

        env = {
            "API_BASE_URL": "https://jsonplaceholder.typicode.com",
            "API_TIMEOUT": "3",
        }

        with patch.dict(os.environ, env, clear=True):
            result = get_config()

        self.assertEqual(result["api_base_url"], "https://jsonplaceholder.typicode.com")
        self.assertEqual(result["api_timeout"], 3)

    def test_fetch_env_value_error(self):
        env = {
            "API_TIMEOUT": "3",
        }

        with patch.dict(os.environ, env, clear=True):
            with self.assertRaises(ValueError):
                get_config()

    def test_fetch_env_empty_base_url(self):
        env = {
            "API_BASE_URL": "",
            "API_TIMEOUT": "3",
        }

        with patch.dict(os.environ, env, clear=True):
            with self.assertRaises(ValueError):
                get_config()


if __name__ == "__main__":
    unittest.main()
