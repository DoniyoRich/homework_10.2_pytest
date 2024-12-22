import logging
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
logs_path = os.path.join(dir_path, '..', 'logs', 'utils.log')

masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler(logs_path, "w", encoding="UTF-8")
file_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску
    в формате XXXX XX** **** XXXX, где X — это цифра номера.
    """
    masks_logger.info(f"Принят номер карты {card_number} для маскирования")
    numbers_list = list(card_number.strip())
    if len(numbers_list) == 0:
        masks_logger.error("Нулевая длина номера карты. Вызвано исключение")
        raise ValueError("Нулевая длина номера карты")
    elif len(numbers_list) == 16:
        for index_ in range(6, 12):
            numbers_list[index_] = "*"
        masks_logger.info("Маскирование номера карты выполнено успешно")
    else:
        masks_logger.error("Нестандартный номер карты, должно быть 16-значное число")
        raise ValueError("Нестандартный номер карты, должно быть 16-значное число")

    # проставляем пробелы каждые четыре разряда
    index_ = 4

    while index_ < len(numbers_list):
        numbers_list.insert(index_, " ")
        index_ += 5
    masked_card = "".join(numbers_list)
    masks_logger.info(f"Карта {card_number} маскирована в виде {masked_card}")
    return masked_card


def get_mask_account(account_number: str) -> str:
    """
    Принимает на вход номер счета и возвращает его маску
    в формате **XXXX, где X — это цифра номера.
    """
    masks_logger.info(f"Получен номер счета {account_number} для маскирования")
    if len(account_number) == 0:
        masks_logger.error("Нулевая длина номера счета")
        raise ValueError("Нулевая длина номера счета")
    elif len(account_number) == 20:
        card_masked = "**" + account_number[-4:]
        masks_logger.info(f"Счет {account_number} маскирован в виде {card_masked}")
        return card_masked
    else:
        masks_logger.error("Нестандартный номер счета, вызвано исключение")
        raise ValueError("Нестандартный номер счета, должно быть 20-значное число")
