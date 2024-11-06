def mask_account_card(string_: str) -> list:
    """Функция выделяет цифры и буквы из строки."""
    digits_start = 0
    for i in range(len(string_)):
        if string_[i].isdigit():
            digits_start = i
            break

    account = []
    account.append(string_[:digits_start].strip())
    account.append(string_[digits_start:].strip())

    return account


def get_date(date_string: str) -> str:
    """Функция форматирует дату, полученную в качестве аргумента"""
    # извлекаем символы до буквы "Т",
    # и преобразуем в список по разделителю "-"
    if date_string.count("-") == 2 and "T" in date_string:
        date_separated = (date_string[: date_string.index("T")]).split("-")
    else:
        print("Неверный формат данных")

    date_formatted = []
    # проходим по списку в обратном порядке
    # и записываем значения в новый список
    for date_element in reversed(date_separated):
        date_formatted.append(date_element)

    return ".".join(date_formatted)
