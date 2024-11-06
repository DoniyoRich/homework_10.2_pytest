def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску
    в формате XXXX XX** **** XXXX, где X — это цифра номера.
    """

    numbers_list = list(card_number.strip())
    for index_ in range(6, 12):
        numbers_list[index_] = "*"

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
    return "**" + account_number[-4:]
