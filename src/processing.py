def filter_by_state(list_dict: list[dict[str, any]], state_: str = "EXECUTED") -> list[dict[str, any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_dict = []
    for i in list_dict:
        if i["state"] == state_:
            new_dict.append(i)
    return new_dict


def sort_by_date(list_: list, is_reverse: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    list_sorted = sorted(list_, key=lambda x: x["date"], reverse=is_reverse)
    return list_sorted
