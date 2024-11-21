import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(list_of_dicts):
    """Тест на фильтрацию списка по значению ключа state, принятом по умолчанию (EXECUTED)."""
    assert filter_by_state(list_of_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_cancelled(list_of_dicts):
    """Тест на фильтрацию списка по значению ключа state = 'CANCELED'."""
    assert filter_by_state(list_of_dicts, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "no_correct_state",
    [
        ({"id": 41428829, "state": "493487ejrh", "date": "2019-07-03T18:35:29.512364"}),
        (
                {
                    "id": 939719570,
                    "state": " --cv.,bmzxv++  ",
                    "date": "2018-06-30T02:08:58.425572",
                }
        ),
        ({"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"}),
        ({"id": 594226727, "date": "2018-09-12T21:27:25.241689"}),
    ],
)
def test_filter_by_state_wrong_state(no_correct_state):
    """Тест на некорректное значение ключа state."""
    with pytest.raises(TypeError):
        filter_by_state(no_correct_state)


def test_sort_by_date_default(list_of_dicts):
    """Тест на сортировку списка словарей по ключу date в порядке убывания."""
    assert sort_by_date(list_of_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_FALSE(list_of_dicts):
    """Тест на сортировку списка словарей по ключу date, принятом по умолчанию (True)."""
    assert sort_by_date(list_of_dicts, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "wrong_date",
    [
        ({"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"}),
        ({"id": 939719570, "state": "EXECUTED", "date": "sd-4epr98643"}),
        ({"id": 939719570, "state": "EXECUTED", "date": "125/45/6546"}),
        ({"id": 939719570, "state": "EXECUTED", "date": ""}),
        ({"id": 939719570, "state": "EXECUTED"}),
    ],
)
def test_sort_by_date_wrong_date(wrong_date):
    """Тест на некорректные форматы дат."""
    with pytest.raises(Exception):
        sort_by_date(wrong_date)
