inform_state = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"}
]


def filter_by_state(inform_state: list[dict[str]], state_id="EXECUTED") -> list[dict[str]] | None:
    """Функция принимает на вход список словарей и значение для ключа
    state и выдает новый список с заданным ключом"""

    list_state = []
    for key in inform_state:
        if key.get("state") == state_id:
            list_state.append(key)

    return list_state


def sort_by_date(inform_state: list[dict[str]], reverse=True) -> list[dict[str]] | None:
    sorted_inform_state = sorted(inform_state, key=lambda inform_state: inform_state["date"], reverse=reverse)
    return sorted_inform_state

