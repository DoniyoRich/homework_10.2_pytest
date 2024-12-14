import json

from src.external_api import convert_curr


def converted_transactions(json_path: str) -> list:
    """ Функция преобразует входящий json объект в список словарей"""

    try:
        with open(json_path, encoding='utf-8') as data:
            transaction_data = data.read()
        return json.loads(transaction_data)
    except FileNotFoundError:
        print("Что-то не так с файлом, или он пустой")
        return []


def transaction_amount(transaction: dict) -> str:
    """
    Функция возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """
    print(f'\nОдна из случайных транзакций:\n {transaction}')
    trans_curr = transaction["operationAmount"]["currency"]["code"]
    trans_amount = transaction['operationAmount']['amount']
    result = trans_amount

    # ecли валюта транзакции не рубль, то обращение к API для конвертации
    if trans_curr != "RUB":
        result = convert_curr(trans_curr, "RUB", trans_amount)
        trans_curr = "RUB"

        if result == -1:
            trans_curr = transaction['operationAmount']['currency']['code']
            result = transaction['operationAmount']['amount']

    return f'\nТранзакция ID: {transaction["id"]}, сумма: {round(float(result), 2)} {trans_curr}'
