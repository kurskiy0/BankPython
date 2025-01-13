from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number: Union[str]) -> str:
    """Функция принимает строку, содержащую тип и номер карты или счета и возвращает строку с замаскированным номером"""
    parts = type_number.split(' ')
    count_str = parts[-1]
    type_str = ' '.join(parts[0:-1])
    if "Счет" in type_number or "Счёт" in type_number:
        answer =  type_str + ' ' + get_mask_account(count_str)
    else:
        answer = type_str + ' ' + get_mask_card_number(count_str)
    return answer


def get_date(date_old: Union[str]) -> str:
    """Функция принимает на вход полную дату и возвращает её в более удобном формате"""
    date_splited = date_old.split("T")
    date_ = date_splited[0].split('-')
    return (f"{date_[-1]}.{date_[-2]}.{date_[-3]}")

print(mask_account_card('Счет 12345678901234567890'))
print(mask_account_card('Visa 1234567890123456'))
print(mask_account_card('Visa Super 1234567890123456'))
print(mask_account_card('Visa Super Puper 1234567890123456'))
print(get_date('2012-11-10T01:02:03.012345'))
