import unittest
from main import parse_json, serialize_json, read_json_file, write_json_file
import json
import tempfile
import os


class TestJson(unittest.TestCase):
    def test_parse_json(self):

        json_data = {
            "users": [
                {"id": 1, "name": "Alice", "role": "data_engineer"},
                {"id": 2, "name": "Bob", "role": "data_analyst"},
            ]
        }

        result = parse_json(json.dumps(json_data))

        self.assertEqual(result, json_data)

    def test_parse_invalid_json(self):

        invalid_json = "{invalid_key: 0}"

        with self.assertRaises(json.JSONDecodeError):
            parse_json(invalid_json)

    def test_serialize_json(self):

        json_data = {
            "users": [
                {"id": 1, "name": "Alice", "role": "data_engineer"},
                {"id": 2, "name": "Bob", "role": "data_analyst"},
            ]
        }

        result = serialize_json(json_data)

        self.assertEqual(result, json.dumps(json_data, indent=4))

    def test_write_json_file(self):
        json_data = {
            "users": [
                {"id": 1, "name": "Alice", "role": "data_engineer"},
                {"id": 2, "name": "Bob", "role": "data_analyst"},
            ]
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = os.path.join(temp_dir, "test_data.json")

            write_json_file(temp_file_path, json_data)
            self.assertTrue(os.path.exists(temp_file_path))

    def test_read_json_file(self):

        json_data = {
            "users": [
                {"id": 1, "name": "Alice", "role": "data_engineer"},
                {"id": 2, "name": "Bob", "role": "data_analyst"},
            ]
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = os.path.join(temp_dir, "test_data.json")

            with open(temp_file_path, "w", encoding="utf-8") as f:
                json.dump(json_data, f)

            result = read_json_file(temp_file_path)
            self.assertEqual(result, json_data)

    def test_read_invalid_json_filei(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = os.path.join(temp_dir, "corrupt.json")

            with open(temp_file_path, "w", encoding="utf-8") as f:
                f.write("{invalid_json:true}")

            with self.assertRaises(json.JSONDecodeError):
                read_json_file(temp_file_path)


if __name__ == "__main__":
    unittest.main()
