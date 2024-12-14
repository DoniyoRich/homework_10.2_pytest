from src.utils import transaction_amount


def test_transaction_amount_rub(some_transaction_rub):
    assert transaction_amount(some_transaction_rub) == "\nТранзакция ID: 939719570, сумма: 9824.07 RUB"


def test_transaction_amount_non_rub(mock_convert_curr, some_transaction_usd):
    # print(mock_responce)
    mock_convert_curr.return_value = 158388.33

    assert transaction_amount(some_transaction_usd) == f"\nТранзакция ID: 939719840, сумма: 158388.33 RUB"
