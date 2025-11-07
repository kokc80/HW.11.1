import os
import unittest
from unittest.mock import patch, mock_open
from src.utils import read_json

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
file_path_data = f"{ROOT_DIR}\\data\\operations_test.json"


trans_test_value = [
    {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {
            "amount": "92688.46",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"
    },
    {
        "id": 957763565,
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534",
        "operationAmount": {
            "amount": "87941.37",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 46363668439560358409",
        "to": "Счет 18889008294666828266"
    },
    {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }
]


@patch('utils.read_json')
def test_read_json(mock_file):
    mock_file.return_value.json.return_value = trans_test_value
    assert read_json(file_path_data) == trans_test_value


def test_read_json_err():
    result = read_json("nofile.json")
    assert result is None


class TestReadJson(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_file_not_found_error(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        result = read_json('non_existent_file.json')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
