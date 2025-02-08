import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_transaction_descriptions(filter_correct):
    assert list(transaction_descriptions(filter_correct)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize("data, expected", [([], []), ([{"id": "555"}], [None])])
def test_transaction_descriptions_corner(data, expected):
    assert list(transaction_descriptions(data)) == expected


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "RUB",
            [
                {
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                },
                {
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                },
            ],
        ),
        (
            "USD",
            [
                {
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                },
                {
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                },
                {
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                },
            ],
        ),
        ("UAN", []),
    ],
)
def test_filter_by_currency(filter_correct, currency, expected):
    assert list(filter_by_currency(filter_correct, currency)) == expected


def test_card_number_generator():
    assert list(card_number_generator(1234, 1236)) == [
        "0000 0000 0000 1234",
        "0000 0000 0000 1235",
        "0000 0000 0000 1236",
    ]


def test_card_number_generator_wrong_direction():
    assert list(card_number_generator(1236, 1234)) == []
