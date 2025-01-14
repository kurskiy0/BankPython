def filter_by_state(list_dict: list[dict], state_string: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_dict = []
    for i in list_dict:
        if i["state"] == state_string:
            new_dict.append(i)
    return new_dict


def sort_by_date(list_date: list, is_reverse: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    list_sorted = sorted(list_date, key=lambda x: x["date"], reverse=is_reverse)
    return list_sorted


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
