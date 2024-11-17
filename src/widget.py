def mask_account_card(string_: str) -> list:
    """Функция выделяет цифры и буквы из строки."""
    digits_start = 0
    account = []
    for i in range(len(string_)):
        # ищем где начинаются цифры
        if string_[i].isdigit():
            # если нашли позицию начала набора цифр, то запоминаем ее индекс и выходим из цикла
            digits_start = i
            break

    # спикок хранит название карты в позиции 0, и номер карты в позиции 1
    account.append(string_[:digits_start].strip())
    account.append(string_[digits_start:].strip())

    if account[0] in [
        "Счет",
        "Maestro",
        "MasterCard",
        "Visa Platinum",
        "Visa Classic",
        "Visa Gold",
    ]:
        if len(account[1]) == 16 or len(account[1]) == 20:
            return account
        else:
            raise ValueError("Неверная длина номера счета или карты")
    elif account == []:
        raise ValueError("Пустые данные")
    else:
        raise ValueError("Несуществующее имя счета или карты")


def get_date(date_string: str) -> str:
    """Функция форматирует дату, полученную в качестве аргумента"""
    # извлекаем символы до буквы "Т",
    # и преобразуем в список по разделителю "-"
    if date_string.count("-") == 2 and "T" in date_string:
        date_separated = (date_string[: date_string.index("T")]).split("-")
    else:
        raise ValueError("Неверный формат данных")

    date_formatted = []
    # проходим по списку в обратном порядке
    # и записываем значения в новый список
    for date_element in reversed(date_separated):
        date_formatted.append(date_element)

    return ".".join(date_formatted)
