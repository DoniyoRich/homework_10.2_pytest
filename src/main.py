import os
from pathlib import Path

from dotenv import load_dotenv

import src.processing
from src.operations import read_from_csv, read_from_excel
from src.output_data import get_descriptions, print_formatted
from src.regex_searching import search_by_pattern
from src.utils import converted_transactions

dir_path = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = str(Path(__file__).parent.parent)
logs_path = os.path.join(dir_path, '..', 'logs', 'main.log')
transactions_path = BASE_DIR + '\\data'

load_dotenv(BASE_DIR + '\\.env')

file_types = {"1": "JSON", "2": "CSV", "3": "XLSX"}
transaction_status = ["EXECUTED", "CANCELED", "PENDING"]


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

        print("Введите статус, по которому необходимо выполнить фильтрацию. "
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING (0 для выхода)")

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
                    f"Статус операции '{transaction_status_choice}' недоступен",
                    "попробуйте еще раз, или 0 для завершения")
                continue

        if not transaction_status_choice == '0':
            filtered_by_state = src.processing.filter_by_state(transactions_list, transaction_status_choice)
            current_state_of_transactions_list = filtered_by_state
            if filtered_by_state:
                print(f"Операции отфильтрованы по статусу '{transaction_status_choice}'")
                is_sorted_by_date_mes = input("\nОтсортировать операции по дате? да/нет(Enter): ")
                if is_sorted_by_date_mes.lower() == "да" or is_sorted_by_date_mes.lower() == "lf":

                    print("Сортировка по дате: да")

                    is_sort_ascending_mes = input("\nПо возрастанию: да/нет(Enter): ")
                    if is_sort_ascending_mes.lower() == "да" or is_sort_ascending_mes.lower() == "lf":
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
                        current_state_of_transactions_list = list(
                            filter(lambda x: x['operationAmount']['currency']['code'] == 'RUB', filtered_only_rubles))
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

                categories = get_descriptions(current_state_of_transactions_list, 'description')

                if len(categories):
                    print("\nРаспечатываю итоговый список транзакций")
                    print(f'Всего банковских операций в выборке: {sum(categories.values())}')
                    # categories = get_descriptions(current_state_of_transactions_list)
                    for key, value in categories.items():
                        print(f"{key}: {value}")

                    print_formatted(current_state_of_transactions_list, file_types.get(source_file_choice))
                else:
                    print('\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации')

            else:
                print("-" * 40)
                print(f"Транзакции со статусом {transaction_status_choice} отсутствуют")


if __name__ == "__main__":
    main()
