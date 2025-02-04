def filter_by_state(list_dict: list[dict], state_string: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_dict = []
    for i in list_dict:
        if not list_dict:
            return "Не введены данные"
        elif i["state"] == state_string:
            new_dict.append(i)
            return new_dict
        else:
            return "State отсутствует в списке словарей"



def sort_by_date(list_date: list, is_reverse: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    list_sorted = sorted(list_date, key=lambda x: x["date"], reverse=is_reverse)
    return list_sorted
