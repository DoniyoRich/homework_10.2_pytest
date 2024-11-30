from collections.abc import Generator


def filter_by_currency(list_trans: list[dict], currency: str) -> Generator[dict]:
    """
    Функция-генератор возвращает итератор, отфильтрованный по ключу 'currency'
    """
    for record in filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, list_trans):
        yield record


def transaction_descriptions(list_trans: list[dict]) -> Generator[str]:
    """Функция-генератор возращает текстовое описание транзакции"""
    if list_trans == []:
        print("11111111111111")
        raise Exception("Неверные или пустые данные")
        print("222222222222222")
    print("333333333333333")


    for descript_ in map(lambda x: x["description"], list_trans):
        yield descript_


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
