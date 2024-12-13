import json
import typing
from idlelib.pyparse import trans
from urllib.parse import urljoin

import requests

from src.external_api import convert_curr
from src.transactions import transactions


def ret_transactions(json_path: str) -> list:
    """ Функция преобразует входящий json объект в список словарей"""

    try:
        with open(json_path, encoding='utf-8') as data:
            transaction_data = data.read()
        return json.loads(transaction_data)
    except FileNotFoundError:
        print("Что-то не так с файлом, или он пустой")
        return []


def transaction_amount(transaction: dict) -> float:
    """
    Функция возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """
    print(f'Одна из транзакций: {transaction}')
    trans_id = transaction['id']

    # тут надо организовать проверку валюты, если не рубль, то обращение к API
    if True:
        # convert_curr()
        pass

    trans_amount = transaction['operationAmount']['amount']
    trans_curr = transaction['operationAmount']['currency']['name']

    print(f'Транзакция ID: {trans_id}, сумма: {trans_amount} {trans_curr}')
