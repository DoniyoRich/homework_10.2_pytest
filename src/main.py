import src.masks
import src.processing
import src.widget


def start() -> None:
    # ТУТ КОД ИЗ ПРЕДЫДУЩЕЙ ДОМАШКИ, НЕ ЗНАЮ, НУЖНО ЛИ БЫЛО ЕГО ОСТАВЛЯТЬ ТУТ ;)
    # ПРИ ЗАПРОСЕ ДАННЫХ НУЖНО ПРОСТО ВВОДИТЬ "0", ЧТОБЫ ПРОПУСТИТЬ
    """
    Основная функция программы. Запрашивает строку,
    содержащую тип и номер карты или счета у Пользователя.
    Корректность ввода данных проверяется в отдельной функции.
    """
    print(
        """
    Программа маскировки номера карты и номера счета Пользователя.
    Маскированный номер карты отображается в следующем формате: XXXX XX** **** XXXX, где X — это цифра номера.
    Маскированный счет отображается следующим образом: **XXXX, где X — последние цифры счета.
    """
    )
    # Запрашиваем строку, содержащую тип и номер карты или счета у Пользователя
    account_or_card = input(
        "Введите строку, содержащую тип и номер карты или счета (0 - пропустить): \n"
    ).strip()

    # account_or_card = "Maestro 1596837868705199"
    # account_or_card = "Счет 64686473678894779589"
    # account_or_card = "MasterCard 7158300734726758"
    # account_or_card = "Счет 35383033474447895560"
    # account_or_card = "Visa Classic 6831982476737658"
    # account_or_card = "Visa Platinum 8990922113665229"
    # account_or_card = "Visa Gold 5999414228426353"
    # account_or_card = "Счет 73654108430135874305"

    if account_or_card != "0":
        try:
            account_separated = src.widget.mask_account_card(account_or_card)
            if account_separated[0] == "Счет":
                print(f"Счёт {src.masks.get_mask_account(account_separated[1])}")
            else:
                print(
                    f"{account_separated[0]} {src.masks.get_mask_card_number(account_separated[1])}"
                )
        except Exception:
            print("Что-то пошло не так.")

    try:
        date_to_format = input(
            "\nВведите неотформатированную строку с датой (0 - пропустить): \n"
        ).strip()
        if date_to_format != "0":
            print(f"Дата: {src.widget.get_date(date_to_format)}")
    except Exception:
        print("Что-то пошло не так.")

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


if __name__ == "__main__":
    start()
