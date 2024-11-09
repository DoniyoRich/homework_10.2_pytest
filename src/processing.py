def filter_by_state(dicts_to_filter: list, state: str = "EXECUTED") -> list:
    """Функция возвращает список словарей по фильтру значения state."""
    filtered_list = []
    for dictionary in dicts_to_filter:
        if dictionary["state"] == state:
            filtered_list.append(dictionary)

    return filtered_list


def sort_by_date(dicts_to_sort: list, rev_sorted: bool = True) -> list:
    """Функция возращает список словарей, отсортированный по дате."""

    return sorted(dicts_to_sort, key=lambda x: x["date"], reverse=rev_sorted)
