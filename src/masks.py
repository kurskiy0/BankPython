from typing import Union


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает его зашифрованный вариант"""
    if len(card_number) == 16:
        str_card_num = str(card_number)
        return " ".join(
            (
                str_card_num[0:4],
                str_card_num[4:6] + "**",
                "****",
                str_card_num[12:16],
            )
        )
    elif len(card_number) != 16:
        return 'Введен некорректный номер карты'
    elif not card_number.isdigit():
        return 'Введен некорректный номер карты'
    return None


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(account_number) == 20:
        str_account_number = str(account_number)
        return "**" + str_account_number[16:]
    elif len(account_number) != 20:
        return 'Введен некорректный номер счета'
    elif not account_number.isdigit():
        return 'Введен некорректный номер счета'
    return None

