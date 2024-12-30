from unittest.mock import patch

from src.main import main


@patch("builtins.input", side_effect=["1", "executed", "да", "да", "да", "да", "вкл"])
def test_main_json(mocked_input):
    """ Тест главной функции. """
    main()


@patch("builtins.input", side_effect=["2", "canceled", "нет", "да", "да", "да", "вкл"])
def test_main_csv(mocked_input):
    """ Тест главной функции. """
    main()


@patch("builtins.input", side_effect=["3", "pending", "да", "нет", "да", "да", "вкл"])
def test_main_xlsx(mocked_input):
    """ Тест главной функции. """
    main()


@patch("builtins.input", side_effect=["0", "pending", "да", "нет", "да", "да", "вкл"])
def test_main_exit_when_file_choice(mocked_input):
    """ Тест главной функции. """
    main()


@patch("builtins.input", side_effect=["2", "0", "да", "нет", "да", "да", "вкл"])
def test_main_exit_when_status(mocked_input):
    """ Тест главной функции. """
    main()


@patch("builtins.input", side_effect=["2", "executed", "да", "нет", "да", "да", ""])
def test_main_no_search(mocked_input):
    """ Тест главной функции. """
    main()


@patch("builtins.input", side_effect=["1", "executed", "да", "нет", "нет", "да", "ыдвлоапр"])
def test_main_wrong_search(mocked_input):
    """ Тест главной функции. """
    main()
