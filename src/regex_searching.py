import re


def search_by_pattern(word: str, transactions: list[dict]) -> list[dict]:
    """ Функция поиска совпадения описания транзакции по слову. """
    # for trans in transactions:
    #     print(re.search(word, trans['description']))
    # input()
    return [dict_ for dict_ in transactions if re.search(word, dict_['description'])]
