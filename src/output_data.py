from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card


def print_formatted(transactions: list, file_type: str) -> None:
    for trans in transactions:
        print()
        if file_type.lower() == 'json':
            amount = trans['operationAmount']['amount']
        else:
            pass
        description = trans['description']
        print(get_date(trans['date']), description)

        if description.lower() == "открытие вклада":
            account_separated = mask_account_card(trans['to'])
            if len(account_separated[1]) == 16:
                account = get_mask_card_number(account_separated[1])
            else:
                account = get_mask_account(account_separated[1])
            print(account_separated[0], account)
            print(trans['amount'])
        else:
            account_separated_from = mask_account_card(trans['from'])

            account_separated_to = mask_account_card(trans['to'])
            print(account_separated_from[0], account_separated_from[1], '->', account_separated_to[0],
                  account_separated_to[1])
