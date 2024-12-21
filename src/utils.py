import json
import logging

from src.external_api import convert_curr

utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def converted_transactions(json_path: str) -> list:
    """ Функция преобразует входящий json объект в список словарей"""

    try:
        utils_logger.info("Попытка прочитать файл json")
        with open(json_path, encoding='utf-8') as data:
            transaction_data = data.read()
        utils_logger.info("Чтение и обработка файла успешна")
        return json.loads(transaction_data)
    except Exception:
        utils_logger.error("Ошибка чтения файла, возвращен пустой список")
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
    utils_logger.info(f"Принята транзакция на обработку, валюта {trans_curr}")

    # ecли валюта транзакции не рубль, то обращение к API для конвертации
    if trans_curr != "RUB":
        result = convert_curr(trans_curr, "RUB", trans_amount)
        trans_curr = "RUB"
        utils_logger.info("Конвертация валюты успешна, возвращена сумма в рублях")

        if result == -1:
            trans_curr = transaction['operationAmount']['currency']['code']
            result = transaction['operationAmount']['amount']
            utils_logger.warning("Конвертация не удалась, сумма возвращена в исходной валюте")

    return f'\nТранзакция ID: {transaction["id"]}, сумма: {round(float(result), 2)} {trans_curr}'
