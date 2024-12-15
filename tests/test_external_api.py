from unittest.mock import patch

from src.external_api import convert_curr


@patch("requests.get")
def test_convert_curr_success(mocked_responce):
    """ Тест на успешное выполнение запроса на конвертацию валюты. """
    print(mocked_responce)
    mocked_responce.return_value.status_code = 200
    mocked_responce.return_value.json.return_value = {"info": {"rate": 100}, "result": 10000}
    assert convert_curr("USD", "RUB", "100") == 10000
    mocked_responce.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100&apikey=None")


@patch("requests.get")
def test_convert_curr_fail(mocked_responce):
    """ Тест на неудачный запрос на конвертацию валюты. """
    print(mocked_responce)
    mocked_responce.return_value.status_code = 400
    assert convert_curr("USD", "RUB", "100") == -1
    mocked_responce.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100&apikey=None")
