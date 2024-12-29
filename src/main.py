import logging
import os
from pathlib import Path

from dotenv import load_dotenv

import src.processing
import src.transactions
from src.operations import read_from_csv, read_from_excel
from src.output_data import print_formatted
from src.regex_searching import search_by_pattern
from src.utils import converted_transactions

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


def user_input(message: str, answers: list) -> str:
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


def main() -> None:
    """ Основная функция программы. """

    print("""\nПривет!
    Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню (0 для выхода):
          1. Получить информацию о транзакциях из JSON - файла.
          2. Получить информацию о транзакциях из CSV - файла.
          3. Получить информацию о транзакциях из XLSX - файла""")

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
            """Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING (0 для выхода)""")

        transaction_status_choice = '0'
        while True:
            try:
                transaction_status_choice = input("\nСтатус операции: ").upper()
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
                else:
                    print("Сортировка по дате: нет")

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
                else:
                    print("Только рублевые транзакции: нет")

                is_word_to_search = input(
                    "\nОтфильтровать список транзакций по определенному слову в описании: да/нет(Enter): ")
                if is_word_to_search.lower() == "да" or is_word_to_search.lower() == "lf":
                    current_state_of_transactions_list = search_by_pattern(input("Введите слово для поиска: "),
                                                                           current_state_of_transactions_list)
                else:
                    print("Поиск по определенному шаблону не производится")

                descriptions = [x["description"] for x in current_state_of_transactions_list]

                if len(descriptions):
                    print("\nРаспечатываю итоговый список транзакций")
                    print(f'Всего банковских операций в выборке: {len(descriptions)}')
                    print_formatted(current_state_of_transactions_list, file_types.get(source_file_choice))
                else:
                    print(f'\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации')

            else:
                print("-" * 40)
                print(f"Транзакции со статусом {transaction_status_choice} отсутствуют")

    # Генерируем номера карт в требуемом диапазоне
    # start_card = 1
    # stop_card = 3
    # for card_number in src.generators.card_number_generator(start_card, stop_card):
    #     print(card_number)


if __name__ == "__main__":
    main()
