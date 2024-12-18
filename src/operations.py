import csv
import logging

import pandas as pd

operations_logger = logging.getLogger("operations")
file_handler = logging.FileHandler(f"../logs/operations.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
operations_logger.addHandler(file_handler)
operations_logger.setLevel(logging.DEBUG)


def read_from_csv(file_path: str) -> list[dict]:
    """ Функция принимает пусть к файлу .csv и возвращает список словарей. """
    try:
        with open(file_path, encoding='utf-8') as file_name:
            reader = csv.DictReader(file_name, delimiter=';')
            operations_logger.info(f"Успешное чтение файла {file_path}")
            return list(reader)
    except FileNotFoundError:
        operations_logger.error(f"Ошибка чтения файла {file_path}")
        return []


def read_from_excel(file_path) -> list[dict]:
    """ Функция принимает пусть к файлу формата excel и возвращает список словарей. """
    try:
        excel_data = pd.read_excel(file_path).to_dict(orient="records")
        operations_logger.info(f"Успешное чтение файла {file_path}")
        return excel_data
    except FileNotFoundError:
        operations_logger.error(f"Ошибка чтения файла {file_path}")
        return []
