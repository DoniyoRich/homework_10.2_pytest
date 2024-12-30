import pytest

from src.regex_searching import search_by_pattern


@pytest.mark.parametrize(
    "word, dict_",
    [
        ("вкл", [
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
        ])
    ]
)
def test_search_by_pattern(list_of_transactions_for_regex, word, dict_):
    assert search_by_pattern(word, list_of_transactions_for_regex) == dict_
