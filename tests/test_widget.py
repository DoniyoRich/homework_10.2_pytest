import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_or_card, separated",
    [
        ("Maestro 1596837868705199", ["Maestro", "1596837868705199"]),
        ("Счет 64686473678894779589", ["Счет", "64686473678894779589"]),
        ("MasterCard 7158300734726758", ["MasterCard", "7158300734726758"]),
        ("Счет 35383033474442789556", ["Счет", "35383033474442789556"]),
        ("Visa Classic 6831982476737658", ["Visa Classic", "6831982476737658"]),
        ("Visa Platinum 8990922113665229", ["Visa Platinum", "8990922113665229"]),
        ("Visa Gold 5999414228426353", ["Visa Gold", "5999414228426353"]),
        ("Счет 73654108430135874305", ["Счет", "73654108430135874305"]),
    ],
)
def test_mask_account_card(account_or_card, separated):
    """Тест на правильность разделения имени счета или карты и самого номера."""
    assert mask_account_card(account_or_card) == separated


@pytest.mark.parametrize(
    "account_or_card_nonst",
    [
        ("1596837868705199"),
        ("Счет 646779589"),
        ("Mad 71583007758"),
        ("eddfdf3538556"),
        ("Vis 68354511321511982476737658"),
        ("inum"),
        ("dfgvb465745"),
        (""),
    ],
)
def test_mask_account_card_nonst(account_or_card_nonst):
    """Тест на корректность входных данных."""
    with pytest.raises(ValueError):
        mask_account_card(account_or_card_nonst)


def test_get_date(some_date):
    """Тест на правильность преобразования даты."""
    assert get_date(some_date) == "30.06.2018"


@pytest.mark.parametrize(
    "date_wrong",
    [
        ("2018-06-30"),
        ("02:08:58.425572"),
        (""),
        ("10.20.30"),
        ("T02:08:58.425572"),
        ("bla bla bla"),
    ],
)
def test_get_date_wrong(date_wrong):
    "Тест на корректность форматы даты"
    with pytest.raises(ValueError) as e:
        get_date(date_wrong)
    assert str(e.value) == "Неверный формат данных"
    print(str(e.value))
