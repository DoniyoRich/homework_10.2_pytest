def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску
    в формате XXXX XX** **** XXXX, где X — это цифра номера.
    """

    numbers_list = list(card_number.strip())
    if len(numbers_list) == 0:
        raise ValueError("Нулевая длина номера карты")
    elif len(numbers_list) == 16:
        for index_ in range(6, 12):
            numbers_list[index_] = "*"
    else:
        raise ValueError("Нестандартный номер карты, должно быть 16-значное число")

    # проставляем пробелы каждые четыре разряда
    index_ = 4

    while index_ < len(numbers_list):
        numbers_list.insert(index_, " ")
        index_ += 5

    return "".join(numbers_list)


def get_mask_account(account_number: str) -> str:
    """
    Принимает на вход номер счета и возвращает его маску
    в формате **XXXX, где X — это цифра номера.
    """
    # numbers_list = list(card_number.strip())
    if len(account_number) == 0:
        raise ValueError("Нулевая длина номера счета")
    elif len(account_number) == 20:
        return "**" + account_number[-4:]
    else:
        raise ValueError("Нестандартный номер счета, должно быть 20-значное число")
