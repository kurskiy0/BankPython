from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает его зашифрованный вариант"""
    str_card_num = str(card_number)
    return " ".join(
        (
            str_card_num[0:4],
            str_card_num[4:6] + "**",
            "****",
            str_card_num[12:16],
        )
    )


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    str_account_number = str(account_number)
    return "**" + str_account_number[16:]


print(get_mask_card_number(12345678901234567890))