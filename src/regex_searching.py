import re
from typing import Any


def search_by_pattern(word: str, transactions: list[Any]) -> list[dict]:
    """ Функция поиска совпадения описания транзакции по слову. """
    return [dict_ for dict_ in transactions if re.search(word, dict_['description'])]
