from collections.abc import Generator


def filter_by_currency(list_trans):
    pass


def transaction_descriptions(list_trans):
    pass


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """
    Функция-генератор возвращает номер карты в формате ХХХХ ХХХХ ХХХХ ХХХХ,
    где X - цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    if start >= 1 and stop <= 9999_9999_9999_9999 and start <= stop:
        for number in range(start, stop + 1):
            card_number = str(number).zfill(16)
            yield card_number[:4] + " " + card_number[4:8] + \
                " " + card_number[8:12] + " " + card_number[12:16]
    else:
        raise ValueError("Некорректный диапазон")
