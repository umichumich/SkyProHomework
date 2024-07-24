from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str | None:
    """Возвращает скрытый номер карты или счета"""
    if "Счет" in account_card:
        account_card_2 = account_card.replace("Счет ", "")
        acc_number = account_card_2
        result = "Счет " + get_mask_account(acc_number)
        return result
    elif "MasterCard" in account_card:
        account_card_2 = account_card.replace("MasterCard ", "")
        card_number = account_card_2
        result = "MasterCard " + get_mask_card_number(card_number)
        return result
    elif "Visa Classic" in account_card:
        account_card_2 = account_card.replace("Visa Classic ", "")
        card_number = account_card_2
        result = "Visa Classic " + get_mask_card_number(card_number)
        return result
    elif "Visa Gold" in account_card:
        account_card_2 = account_card.replace("Visa Gold ", "")
        card_number = account_card_2
        result = "Visa Gold " + get_mask_card_number(card_number)
        return result
    elif "Visa Platinum" in account_card:
        account_card_2 = account_card.replace("Visa Platinum ", "")
        card_number = account_card_2
        result = "Visa Platinum " + get_mask_card_number(card_number)
        return result
    elif "Maestro" in account_card:
        account_card_2 = account_card.replace("Maestro ", "")
        card_number = account_card_2
        result = "Maestro " + get_mask_card_number(card_number)
        return result
    elif "МИР" in account_card:
        account_card_2 = account_card.replace("МИР ", "")
        card_number = account_card_2
        result = "МИР " + get_mask_card_number(card_number)
        return result
    else:
        return None


def get_date(input_date: str) -> str | None:
    """Возвращает текущюю дату"""
    date = input_date.split("Т")[0]
    formatted_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
    return formatted_date


#input_date = input("Введите данные с текущей датой: ")
#account_card = input("Введите ваши банковские данные: ")

#print(mask_account_card(account_card))
#print(get_date(input_date))
