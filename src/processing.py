from typing import Any


def filter_by_state(dicts_to_filter: list, state: str = "EXECUTED") -> list[Any] | None:
    """Функция возвращает список словарей по фильтру значения state."""
    filtered_list = []
    for dictionary in dicts_to_filter:
        try:
            if dictionary["state"] == state:
                filtered_list.append(dictionary)
        except KeyError:
            print("Некорректный статус")

    if filtered_list != []:
        return filtered_list
    else:
        print("Некорректный статус")
        return None


def sort_by_date(dicts_to_sort: list, rev_sorted: bool = True) -> list:
    """Функция возращает список словарей, отсортированный по дате."""
    try:
        return sorted(dicts_to_sort, key=lambda x: x["date"], reverse=rev_sorted)
    except Exception:
        print("Что то не так с форматом даты")
        raise Exception
