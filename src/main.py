import masks
import widget


def start() -> None:
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
            account_separated = widget.mask_account_card(account_or_card)
            if account_separated[0] == "Счет":
                print(f"Счёт {masks.get_mask_account(account_separated[1])}")
            else:
                print(
                    f"{account_separated[0]} {masks.get_mask_card_number(account_separated[1])}"
                )
        except Exception:
            print("Что-то пошло не так.")

    # date_to_format = "2024-03-11T02:26:18.671407"
    try:
        date_to_format = input(
            "\nВведите неотформатированную строку с датой (0 - выход): \n"
        ).strip()
        if date_to_format != "0":
            print(f"Дата: {widget.get_date(date_to_format)}")
    except Exception:
        print("Что-то пошло не так.")


if __name__ == "__main__":
    start()
