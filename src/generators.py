def filter_by_currency(transactions_list, currency):
    if len(transactions_list) > 0:
        filtered_transactions = filter(
            lambda transactions_list: transactions_list.get("operationAmount").get("currency").get("code") == currency, transactions_list)
        return filtered_transactions
    else:
        return "Список пустой!"
