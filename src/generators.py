from typing import Union, Iterable


def filter_by_currency(transactions: Union[list, dict], currency: str) -> Iterable:
    if not transactions:
        raise ValueError('Отсутствует значение')
    yield (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["name"] == currency
    )


def transaction_descriptions(transactions: list) -> Iterable:
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterable:
    for n in range(start, end):
        card_number = str(n)
        while len(card_number) < 16:
            card_number = "0" + card_number
        yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
