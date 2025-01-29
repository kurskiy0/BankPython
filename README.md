# Проект PythonProjectBank
## Описание
Проект PythonProjectBank - это виджет, который показывает несколько последних успешных банковских операций клиента.
## Установка
1. Колнируйте репозиторий:
```git clone git@github.com:kurskiy0/PythonProjectBank.git```
3. Установите зависимости
```pip install -r requirements.txt```
## Примеры использования
1. Функции в модуле masks.py
```print(get_mask_card_number(12345678901234567890))```
```print(get_mask_account(12345678901234567890))```
2. Функции в модуле widget.py
```print(mask_account_card('Счет 12345678901234567890'))```
```print(get_date('2012-11-10T01:02:03.012345'))```
3. Функции в модуле processing.py
```print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))```
```print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))```
## Тестирование
Проект покрыт тестами. Для их запуска выполните команду
```poetry run pytest --cov```
