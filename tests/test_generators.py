import pytest

from src.generators import card_number_generator


def test_filter_by_currency():
    pass


def test_transaction_descriptions():
    pass


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
    with pytest.raises(ValueError):
        cards_wrong = card_number_generator(start_wrong, stop_wrong)
        assert next(cards_wrong)
