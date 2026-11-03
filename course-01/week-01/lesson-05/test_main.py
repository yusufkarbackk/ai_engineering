import unittest
from unittest.mock import patch, Mock

from main import fetch_todo, Todo


class TestFetchTodo(unittest.TestCase):

    @patch("main.requests.get")
    def test_fetch_todo_success(self, mock_get):
        # Siapkan response palsu
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False,
        }
        mock_get.return_value = mock_response

        # Jalankan fungsi yang diuji
        result = fetch_todo(1)

        # Periksa hasilnya
        self.assertIsInstance(result, Todo)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.title, "delectus aut autem")

        # Pastikan request menggunakan timeout
        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/todos/1",
            timeout=5,
        )


if __name__ == "__main__":
    unittest.main()
    