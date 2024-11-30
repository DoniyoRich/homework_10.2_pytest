import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


@pytest.mark.parametrize(
    "filtered_dict",
    [
        ({
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }),
        ({
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }),
        ({
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        })
    ]
)
def test_filter_by_currency(list_of_transactions, filtered_dict):
    "Тест на правильность получения транзакций по ключу 'currency'"
    gen = filter_by_currency(list_of_transactions, "USD")
    next(gen)


def test_filter_by_currency_no_curr(list_of_transactions_no_curr):
    "Тест на ошибку при отсутствии данных о валюте"
    with pytest.raises(Exception):
        gen = filter_by_currency(list_of_transactions_no_curr, "USD")
        next(gen)


def test_filter_by_currency_wrong(list_of_transactions_empty):
    "Тест на ошибку при пустых данных"
    with pytest.raises(Exception):
        gen = filter_by_currency(list_of_transactions_empty, "USD")
        next(gen)


def test_transaction_descriptions(list_of_transactions):
    "Тест на правильность получения описания транзакции"
    for ind, description_received in enumerate(transaction_descriptions(list_of_transactions)):
        assert description_received == list_of_transactions[ind]["description"]


def test_transaction_descriptions_empty(list_of_transactions_empty):
    "Тест на пустые данные"
    with pytest.raises(Exception):
        gen = transaction_descriptions(list_of_transactions_empty)
        next(gen)


@pytest.mark.parametrize(
    "start_number, stop_number, cards_finished",
    [
        (1, 3,
         ["0000 0000 0000 0001",
          "0000 0000 0000 0002",
          "0000 0000 0000 0003"
          ]
         ),
        (9999_9999_9999_9997,
         9999_9999_9999_9999,
         ["9999 9999 9999 9997",
          "9999 9999 9999 9998",
          "9999 9999 9999 9999"
          ]
         ),
        (255001,
         255003,
         ["0000 0000 0025 5001",
          "0000 0000 0025 5002",
          "0000 0000 0025 5003"
          ]
         )
    ]
)
def test_card_number_generator(start_number, stop_number, cards_finished):
    "Тест на правильность генерирования номера карты"
    card_number = card_number_generator(start_number, stop_number)

    for ind, number in enumerate(card_number):
        assert number == cards_finished[ind]


@pytest.mark.parametrize(
    "start_wrong, stop_wrong",
    [
        (-1, -3),
        (2, -2),
        (-10, -10),
        (9999_9999_9999_9999_9, 5),
        (10, 9999_9999_9999_9999_9),
        (9999_9999_9999_9999_9, 9999_9999_9999_9999_9)
    ]
)
def test_card_number_generator_wrong(start_wrong, stop_wrong):
    "Тест на некорректность диапазона для генерирования карт"
    with pytest.raises(ValueError):
        cards_wrong = card_number_generator(start_wrong, stop_wrong)
        assert next(cards_wrong)
