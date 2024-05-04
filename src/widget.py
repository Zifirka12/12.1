from datetime import datetime
from src.masks import mask_account, mask_card


def mask_number(input_str: str) -> str:
    """
    Принимает на вход строку с информацией — тип карты/счета и номер карты/счета.
    Возвращает исходную строку с замаскированным номером карты/счета.
    """
    split_str = input_str.split()
    if split_str[0] in ["Visa", "MasterCard", "Maestro"]:
        return " ".join([*filter(str.isalpha, split_str), mask_card("".join([i for i in split_str if i.isdigit()]))])
    elif split_str[0] == "Счет":
        return "Счет " + mask_account(split_str[1])
    else:
        return input_str


def convert_date_format(input_str: str) -> str:
    """
    Функция, которая принимает на вход строку вида 2018-07-11T02:26:18.671407
    и возвращает строку с датой.
    """
    input_date = datetime.strptime(input_str, "%Y-%m-%dT%H:%M:%S.%f")
    return input_date.strftime("%d.%m.%Y")
