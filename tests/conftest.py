import pytest


@pytest.fixture
def card_num():
    return "Введен некорректный номер карты"


@pytest.fixture
def account_num():
    return "Введен некорректный номер счета"


@pytest.fixture
def card_zero():
    return " Введен некорректный номер карты"


@pytest.fixture
def card_account():
    return "Счет **7890"


@pytest.fixture
def card_visa():
    return "Visa 1234 56** **** 3456"


@pytest.fixture
def card_another():
    return "Visa Super Puper 1234 56** **** 3456"


@pytest.fixture
def date_get():
    return "10.11.2012"


@pytest.fixture
def date_slash():
    return "10.11.2012"


@pytest.fixture
def date_zero():
    return "Некорректный формат даты"


@pytest.fixture
def state_executed():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def state_zero():
    return "State отсутствует в списке словарей"


@pytest.fixture
def state_empty():
    return "Не введены данные"


@pytest.fixture
def date_empty():
    return "Не введены данные"


@pytest.fixture
def date_out():
    return "Отсутствует дата"


@pytest.fixture
def filter_correct():
    return [
        {
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации"
        },
        {
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет"
        },
        {
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет"
        },
        {
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
        },
        {
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации"
        },
    ]
