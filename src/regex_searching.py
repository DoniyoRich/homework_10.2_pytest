import re


def search_by_pattern(word: str, transactions: list[dict]) -> list[dict]:
    dict_list = []
    for dict_ in transactions:
        match = re.search(word, dict_['description'])
        if match:
            dict_list.append(dict_)

    return dict_list
