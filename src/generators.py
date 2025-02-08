from typing import Union, Iterator
from src.main import transactions


def filter_by_currency(transactions: Union[list, dict], currency: str) -> Iterator:
    return (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )


def transaction_descriptions(transactions: list) -> Iterator:
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, end: int) -> Iterator:
    for n in range(start, end + 1):
        card_number = str(n).zfill(16)
        yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"


if __name__ == "__main__":
    my_descriptions = transaction_descriptions(transactions)
    print(next(my_descriptions))
    print(next(my_descriptions))
