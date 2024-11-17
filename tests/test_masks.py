import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, masked",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(card_number, masked):
    """Тест на правильность маскирования номера карты."""
    assert get_mask_card_number(card_number) == masked


def test_get_mask_card_number_empty(card_number_empty):
    """Тест на отсутствие номера номера карты."""
    with pytest.raises(ValueError) as e:
        get_mask_card_number(card_number_empty)
    assert str(e.value) == "Нулевая длина номера карты"
    print(str(e.value))


@pytest.mark.parametrize(
    "card_number_nonst",
    [
        ("-1502398039483094853496868705199"),
        ("-70734726758"),
        ("688"),
        ("89909"),
        ("599948426353"),
    ],
)
def test_get_mask_card_number_nonstandard(card_number_nonst):
    """Тест на корректность входных данных, длины номера карты."""
    with pytest.raises(ValueError) as e:
        get_mask_card_number(card_number_nonst)
    assert str(e.value) == "Нестандартный номер карты, должно быть 16-значное число"
    print(str(e.value))


@pytest.mark.parametrize(
    "account_number, masked",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(account_number, masked):
    """Тест на правильность маскирования номера счета."""
    assert get_mask_account(account_number) == masked


def test_get_mask_account_empty(mask_account_empty):
    """Тест на отсутствие номера номера карты."""
    with pytest.raises(ValueError) as e:
        get_mask_account(mask_account_empty)
    assert str(e.value) == "Нулевая длина номера счета"
    print(str(e.value))


@pytest.mark.parametrize(
    "account_number_nonst",
    [
        ("-1502398039483094853496868705199"),
        ("-70734726758"),
        ("688"),
        ("89909"),
        ("599948426353"),
    ],
)
def test_get_mask_account_nonstandard(account_number_nonst):
    """Тест на корректность входных данных, длины номера счета."""
    with pytest.raises(ValueError) as e:
        get_mask_account(account_number_nonst)
    assert str(e.value) == "Нестандартный номер счета, должно быть 20-значное число"
    print(str(e.value))
