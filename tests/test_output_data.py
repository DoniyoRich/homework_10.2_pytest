from unittest.mock import patch

from src.output_data import format_output, get_descriptions


def test_format_output_otcr_vklad(capsys):
    dict_ = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    format_output(dict_, '31957.58', 'Открытие вклада', 'руб.')
    captured = capsys.readouterr()
    assert captured.out == (
        "----------------------------------------\n"
        "26.08.2019 Открытие вклада\n"
        "Статус транзакции:  EXECUTED\n"
        "Счет **9589\n"
        "Сумма:  31957.58 руб.\n")


def test_format_output_ne_vklad(capsys):
    dict_ = {
        "id": 847259485,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308798378707170",
        "to": "Счет 64686473678894778612"
    }
    format_output(dict_, '97853.86', 'Перевод с карты на счет', 'руб.')
    captured = capsys.readouterr()
    assert captured.out == (
        "----------------------------------------\n"
        "26.08.2019 Перевод с карты на счет\n"
        "Статус транзакции:  EXECUTED\n"
        "Maestro 1308 79** **** 7170 -> Счет **8612\n"
        "Сумма:  97853.86 руб.\n")


@patch('src.output_data.Counter')
def test_get_descriptions(mocked_Counter):
    mocked_Counter.return_value = {"Открытие вклада": 2}
    test_data = [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        }
    ]
    assert get_descriptions(test_data, 'description') == {"Открытие вклада": 2}
