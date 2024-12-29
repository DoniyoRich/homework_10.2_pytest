import logging
import os
import re
from base64 import decode
from collections import Counter
from doctest import debug_script
from random import randint
from time import perf_counter
from typing import final

from dotenv import load_dotenv
from pyexpat.errors import messages

# import src.generators
# import src.masks
import src.processing
import src.transactions
# import src.widget
from src.output_data import print_formatted
from src.operations import read_from_csv, read_from_excel
from src.processing import sort_by_date
from src.regex_searching import search_by_pattern
from src.transactions import transactions
from src.utils import converted_transactions, transaction_amount
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = str(Path(__file__).parent.parent)
logs_path = os.path.join(dir_path, '..', 'logs', 'main.log')
transactions_path = BASE_DIR + '\\data'

main_logger = logging.getLogger("main")
file_handler = logging.FileHandler(logs_path, "w", encoding="UTF-8")
file_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
main_logger.addHandler(file_handler)
main_logger.setLevel(logging.DEBUG)

load_dotenv(BASE_DIR + '\\.env')

file_types = {"1": "JSON", "2": "CSV", "3": "XLSX"}
transaction_status = ["EXECUTED", "CANCELED", "PENDING"]


def user_input(message: str, answers: list) -> str | bool:
    user_choice = '0'
    while user_choice == '0':
        try:
            user_choice = input(message)
            if user_choice.upper() in answers:
                return user_choice
            else:
                continue
        except Exception:
            print("Некорректный ввод, попробуйте еще раз, или 0 для завершения")
            continue

    return user_choice


def start() -> None:
    """
    Основная функция программы. Запрашивает строку,
    содержащую тип и номер карты или счета у Пользователя.
    Корректность ввода данных проверяется в отдельной функции.
    """

    # date_to_format = "2018-06-30T02:08:58.425572"
    # print(f"Дата: {src.widget.get_date(date_to_format)}")
    #
    # dict_to_operate = [
    #     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    #     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    # ]

    # # Фильтруем и получаем новый список словарей по ключу 'state'
    # filtered_list = src.processing.filter_by_state(dict_to_operate, "CANCELED")
    # print(f"Исходный список словарей:\n {dict_to_operate}")
    # print(f"Отфильтрованный список словарей по ключу 'state':\n {filtered_list}")

    # Сортируем по ключу 'date'
    # print(
    #     f"\nОтсортированный список словарей по ключу 'date':\n, {src.processing.sort_by_date(dict_to_operate, True)}"
    # )
    #
    # # Далее код домашки 11.1 - Генераторы
    # print()
    #
    # currency = ["USD", "RUB"]
    #
    # trans_data = src.transactions.transactions

    # Получаем итератор, отфильтрованный по ключу 'currency'

    # filtered_by_currency = src.generators.filter_by_currency(trans_data, currency[0])
    # for element in filtered_by_currency:
    #     print(element)
    #
    # print()
    # # Получаем текстовые описания транзакций
    #
    # descriptions = src.generators.transaction_descriptions(trans_data)
    # for descript_ in descriptions:
    #     print(descript_)

    print()
    # Генерируем номера карт в требуемом диапазоне
    start_card = 1
    stop_card = 3
    for card_number in src.generators.card_number_generator(start_card, stop_card):
        print(card_number)

    # Домашка 12.1 JSON, requests, HTTP
    # data_path = '../data/operations.json'
    # data_path = ''

    # Получаем список словарей из файла json
    # transactions_list = converted_transactions(data_path)

    # Получаем какую-нибудь рандомную транзакцию из ранее полученного списка
    # if transactions_list:
    #     some_transaction = transactions_list[round(randint(0, len(transactions_list) - 1))]
    #     print(transaction_amount(some_transaction))
    # else:
    #     print("Данных нет")

    # Домашка по csv и pandas
    print()
    start_dir = '../data/'
    files_to_read = ['transactions.csv', 'transactions_excel.xlsx']

    csv_dataset = read_from_csv(start_dir + files_to_read[0])
    print(csv_dataset)
    print()

    excel_dataset = read_from_excel(start_dir + files_to_read[1])
    print(excel_dataset)


if __name__ == "__main__":

    print("""\nПривет!
    Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню (0 для выхода):
          1. Получить информацию о транзакциях из JSON - файла.
          2. Получить информацию о транзакциях из CSV - файла.
          3. Получить информацию о транзакциях из XLSX - файла""")

    # source_file_choice = user_input("\nИз какого файла брать данные? ", file_types)
    source_file_choice = '0'
    while True:
        try:
            source_file_choice = input("\nИз какого файла брать данные? ")
            if source_file_choice in file_types or source_file_choice == "0":
                break
        except Exception:
            print("Некорректный ввод, попробуйте еще раз, или 0 для завершения")
            continue
        else:
            print("Пожалуйста, выберите файл, нажав 1, 2, 3 или 0 для завершения")
            continue

    if not source_file_choice == '0':
        print(f"Для обработки выбран {file_types.get(source_file_choice)}-файл\n")

        transactions_list = []
        if source_file_choice == '1':
            file = r'\operations.json'
            transactions_list = converted_transactions(transactions_path + file)
        elif source_file_choice == '2':
            file = r'\transactions.csv'
            transactions_list = read_from_csv(transactions_path + file)
        elif source_file_choice == '3':
            file = r'\transactions_excel.xlsx'
            transactions_list = read_from_excel(transactions_path + file)

        print(
            """Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

        # transaction_status_choice = user_input("Статус операции: ", transaction_status)
        transaction_status_choice = '0'
        while True:
            try:
                # transaction_status_choice = input("\nСтатус операции: ").upper()
                transaction_status_choice = 'EXECUTED'
                if transaction_status_choice in transaction_status or transaction_status_choice == "0":
                    break
            except Exception:
                print("Некорректный ввод, попробуйте еще раз, или 0 для завершения")
                continue
            else:
                print(
                    f"Статус операции '{transaction_status_choice}' недоступен, попробуйте еще раз, или 0 для завершения")
                continue

        if not transaction_status_choice == '0':
            filtered_by_state = src.processing.filter_by_state(transactions_list, transaction_status_choice)
            current_state_of_transactions_list = filtered_by_state
            if filtered_by_state:
                print(f"Операции отфильтрованы по статусу '{transaction_status_choice}'")
                # print(filtered_by_state)
                is_sorted_by_date = input("\nОтсортировать операции по дате? да/нет(Enter): ")
                if is_sorted_by_date.lower() == "да" or is_sorted_by_date.lower() == "lf":
                    is_sorted_by_date = True

                    print("Сортировка по дате: да")

                    is_sort_ascending = input("\nПо возрастанию: да/нет(Enter): ")
                    if is_sort_ascending.lower() == "да" or is_sort_ascending.lower() == "lf":
                        is_sort_ascending = False
                        print("Выбрана сортировка по возрастанию")
                    else:
                        print("Выбрана сортировка по убыванию")
                        is_sort_ascending = True

                    sorted_by_date = src.processing.sort_by_date(filtered_by_state, is_sort_ascending)
                    current_state_of_transactions_list = sorted_by_date
                    for dict_ in sorted_by_date:
                        print(dict_)

                only_roubles = input("\nВыводить только рублевые транзакции? да/нет(Enter): ")
                if only_roubles.lower() == "да" or only_roubles.lower() == "lf":
                    print("Только рублевые транзакции: да")
                    filtered_only_rubles = current_state_of_transactions_list
                    if file_types.get(source_file_choice) == "JSON":
                        current_state_of_transactions_list = list(filter(
                            lambda x: x['operationAmount']['currency']['code'] == 'RUB',
                            filtered_only_rubles))
                    else:
                        current_state_of_transactions_list = list(filter(
                            lambda x: x['currency_code'] == 'RUB',
                            filtered_only_rubles))

                    for dict_ in current_state_of_transactions_list:
                        print(dict_)

                is_word_to_search = input(
                    "\nОтфильтровать список транзакций по определенному слову в описании: да/нет(Enter): ")
                if is_word_to_search.lower() == "да" or is_word_to_search.lower() == "lf":
                    current_state_of_transactions_list = search_by_pattern(input("Введите слово для поиска: "),
                                                                           current_state_of_transactions_list)
                    for dict_ in current_state_of_transactions_list:
                        print(dict_)
                else:
                    print("Поиск по определенному шаблону не производится")
                    only_roubles = False

                descriptions = [x["description"] for x in current_state_of_transactions_list]
                print(descriptions)
                counted = Counter(descriptions)
                print(counted)

                print("Распечатываю итоговый список транзакций")
                print(f'Всего банковских операций в выборке: {len(descriptions)}')
                print_formatted(current_state_of_transactions_list, source_file_choice)

            else:
                print(f"Транзакции со статусом {transaction_status_choice} отсутствуют")
