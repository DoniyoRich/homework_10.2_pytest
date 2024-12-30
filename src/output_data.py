from collections import Counter
from typing import Any

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card


def format_output(dict_to_process: dict, amount: str, description: str, currency: str) -> None:
    """ Функция форматирует вывод"""
    print("-" * 40)
    print(get_date(dict_to_process['date']), description)
    print("Статус транзакции: ", dict_to_process['state'])

    if description.lower() == "открытие вклада":
        account_separated = mask_account_card(dict_to_process['to'])
        if len(account_separated[1]) == 16:
            account = get_mask_card_number(account_separated[1])
        else:
            account = get_mask_account(account_separated[1])
        print(account_separated[0], account)

    else:
        account_separated_from = mask_account_card(dict_to_process['from'])
        account_separated_to = mask_account_card(dict_to_process['to'])

        if len(account_separated_from[1]) == 16:
            account_masked_from = get_mask_card_number(account_separated_from[1])
        else:
            account_masked_from = get_mask_account(account_separated_from[1])

        if len(account_separated_to[1]) == 16:
            account_masked_to = get_mask_card_number(account_separated_to[1])
        else:
            account_masked_to = get_mask_account(account_separated_to[1])

        print(account_separated_from[0], account_masked_from, '->', account_separated_to[0],
              account_masked_to)

    print("Сумма: ", amount, currency)


def print_formatted(transactions: list[Any], file_type: str | None) -> None:
    """ Функция готовит данные в зависимости от формата файла для печати в заданном формате. """
    for trans in transactions:
        if file_type == 'JSON':
            amount = trans["operationAmount"]['amount']
            description = trans['description']
            currency = trans["operationAmount"]["currency"]["name"]

        else:
            amount = trans['amount']
            description = trans['description']
            currency = trans["currency_name"]

        format_output(trans, amount, description, currency)


def get_descriptions(transactions: list[dict], descr: str) -> dict:
    """ Функция печатает категории и их количество. """
    descriptions = [x[descr] for x in transactions]
    categories = Counter(descriptions)
    return dict(categories)
