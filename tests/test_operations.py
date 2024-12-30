from unittest.mock import mock_open, patch

from src.operations import read_from_csv, read_from_excel


@patch("builtins.open", new_callable=mock_open,
       read_data='id;state;date;amount;currency_name\n3176764;CANCELED;2022-08-24T14:32:38Z;16652;Euro')
def test_read_from_csv(mock_file):
    """ Тест проверки считывания файла формата csv. """
    mock_csv_file = read_from_csv("../data/transactions.csv")
    converted_to_dict = [
        {"id": "3176764",
         "state": "CANCELED",
         "date": "2022-08-24T14:32:38Z",
         "amount": "16652",
         "currency_name": "Euro"}
    ]
    assert mock_csv_file == converted_to_dict


@patch("builtins.open", new_callable=mock_open, read_data='')
def test_read_from_csv_empty(mock_file):
    """ Тест проверки считывания пустого файла формата csv. """
    mock_csv_file = read_from_csv("../data/transactions.csv")
    assert mock_csv_file == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_from_csv_no_file(mock_file):
    """ Тест на отсутствие файла формата csv. """
    mock_no_file = read_from_csv("")
    assert mock_no_file == []


@patch('src.operations.pd.read_excel')
def test_read_from_excel(mock_excel_file):
    """ Тест проверки считывания файла формата excel. """
    mock_excel_file.return_value.to_dict.return_value = \
        [
            {"id": "3176764",
             "state": "CANCELED",
             "date": "2022-08-24T14:32:38Z",
             "amount": "16652",
             "currency_name": "Euro"}
        ]

    assert read_from_excel("../data/transactions_excel.xlsx") == [
        {"id": "3176764",
         "state": "CANCELED",
         "date": "2022-08-24T14:32:38Z",
         "amount": "16652",
         "currency_name": "Euro"}
    ]


@patch("builtins.open", new_callable=mock_open, read_data='')
def test_read_from_excel_empty(mock_file):
    """ Тест проверки считывания пустого файла формата excel. """
    mock_csv_file = read_from_csv("")
    assert mock_csv_file == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_from_excel_no_file(mock_file):
    """ Тест на отсутствие файла формата excel. """
    mock_no_file = read_from_csv('owiueyr.xlsx')
    assert mock_no_file == []
