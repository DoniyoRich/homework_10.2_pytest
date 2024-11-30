import pytest

from src.generators import card_number_generator, transaction_descriptions


def test_filter_by_currency():
    pass


def test_transaction_descriptions(list_of_transactions):
    "Тест на правильность получения описания транзакции"
    for ind, description_received in enumerate(transaction_descriptions(list_of_transactions)):
        assert description_received == list_of_transactions[ind]["description"]


def test_transaction_descriptions_empty(list_of_transactions_empty):
    "Тест на пустые данные"
    with pytest.raises(Exception):
        transaction_descriptions(list_of_transactions_empty)


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
