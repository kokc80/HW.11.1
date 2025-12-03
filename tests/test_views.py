from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

from src.views import read_sett, str_greeting


class TestReadSett(TestCase):

    @patch("src.views.read_json", autospec=True)
    def test_read_sett(self, mock_read_json):
        # Ожидаемые данные
        expected_data = [
            {
                'user_currencies': ['USD', 'EUR'],
                'user_stocks': ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']
            }
        ]
        # Настройка мока
        mock_read_json.return_value = expected_data
        # Выполнение теста
        result = read_sett("test.csv")
        # Проверки
        self.assertEqual(result, expected_data)
        mock_read_json.assert_called_once_with("test.csv")


class TestGreeting(TestCase):
    @patch('datetime.datetime', autospec=True)
    def test_morning_greeting(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2025, 11, 30, 8, 0)
        self.assertEqual(str_greeting(), "Доброе утро")
    @patch('datetime.datetime', autospec=True)
    def test_day_greeting(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2025, 11, 30, 14, 0)
        self.assertEqual(str_greeting(), "Добрый день")
    @patch('datetime.datetime', autospec=True)
    def test_evening_greeting(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2025, 11, 30, 18, 0)
        self.assertEqual(str_greeting(), "Добрый вечер")
    @patch('datetime.datetime', autospec=True)
    def test_night_greeting(self, mock_datetime):
        # Проверка ночного времени
        mock_datetime.now.return_value = datetime(2025, 11, 30, 22, 0)
        self.assertEqual(str_greeting(), "Доброй ночи")
        # Проверка раннего утра
        mock_datetime.now.return_value = datetime(2025, 11, 30, 4, 0)
        self.assertEqual(str_greeting(), "Доброй ночи")


if __name__ == '__main__':
    unittest.main()