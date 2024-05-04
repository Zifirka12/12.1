from src.masks import mask_account, mask_card
from src.widget import convert_date_format, mask_number

card_number = input("Введите номер карты: ")
masked_card = mask_card(card_number)
print(masked_card)

account_number = input("Введите номер счета: ")
masked_account = mask_account(account_number)
print(masked_account)

card_number = input("Введите номер карты: ")
masked_card = mask_number(card_number)
print(masked_card)  # Выведет маскированный номер карты

account_number = input("Введите номер счета: ")
masked_account = mask_number(account_number)
print(masked_account)  # Выведет маскированный номер счета

date_str = input("Введите дату: ")  # "2018-07-11T02:26:18.671407"
print(convert_date_format(date_str))  # 11.07.2018

# data = [
#     "Maestro 1596837868705199",
#     "Счет 64686473678894779589",
#     "MasterCard 7158300734726758",
#     "Счет 35383033474447895560",
#     "Visa Classic 6831982476737658",
#     "Visa Platinum 8990922113665229",
#     "Visa Gold 5999414228426353",
#     "Счет 73654108430135874305"
# ]
#
# Применяем функцию к каждому примеру и выводим результат
# for item in data:
#     hidden_data = mask_number(item)
#     print(hidden_data)
