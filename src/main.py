import src.generators
import src.masks
import src.processing
import src.transactions
import src.widget


def start():
    """
    Основная функция программы. Запрашивает строку,
    содержащую тип и номер карты или счета у Пользователя.
    Корректность ввода данных проверяется в отдельной функции.
    """
    account_or_card = "Maestro 1596837868705199"

    account_separated = src.widget.mask_account_card(account_or_card)
    if account_separated[0] == "Счет":
        print(f"Счёт {src.masks.get_mask_account(account_separated[1])}")
    else:
        print(
            f"{account_separated[0]} {src.masks.get_mask_card_number(account_separated[1])}"
        )

    date_to_format = "2018-06-30T02:08:58.425572"
    print(f"Дата: {src.widget.get_date(date_to_format)}")

    dict_to_operate = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    # Фильтруем и получаем новый список словарей по ключу 'state'
    filtered_list = src.processing.filter_by_state(dict_to_operate, "CANCELED")
    print(f"Исходный список словарей:\n {dict_to_operate}")
    print(f"Отфильтрованный список словарей по ключу 'state':\n {filtered_list}")

    # Сортируем по ключу 'date'
    print(
        f"\nОтсортированный список словарей по ключу 'date':\n, {src.processing.sort_by_date(dict_to_operate, True)}"
    )

    # Далее код домашки 11.1 - Генераторы
    print()

    currency = ["USD", "RUB"]

    trans_data = src.transactions.transactions

    # Получаем итератор, отфильтрованный по ключу 'currency'
    filtered_by_currency = src.generators.filter_by_currency(trans_data, currency[1])
    for element in filtered_by_currency:
        print(element)

    print()
    # Получаем текстовые описания транзакций
    descriptions = src.generators.transaction_descriptions(trans_data)
    for descript_ in descriptions:
        print(descript_)

    print()
    # Генерируем номера карт в требуемом диапазоне
    start_card = 1
    stop_card = 3
    for card_number in src.generators.card_number_generator(start_card, stop_card):
        print(card_number)


if __name__ == "__main__":
    start()
