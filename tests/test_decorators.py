from src.decorators import log


def test_log_decorator():
    """ Тест декоратора при выводе информации в указанный файл. """

    @log(filename="log_test.txt")
    def my_function(x: float, y: float) -> float:
        return x / y

    my_function(6, 2)
    with open("log_test.txt") as file:
        message = file.read()
        assert message == "*my_function* started.\n*my_function* ok. Result is: 3.0\n*my_function* stopped."


def test_log_decorator_console(capsys):
    """ Тест декоратора при выводе информации в консоль. """

    @log()
    def my_function(x: float, y: float) -> float:
        return x / y

    my_function(6, 2)
    captured = capsys.readouterr()
    assert captured.out == "*my_function* started.\n*my_function* ok. Result is: 3.0\n*my_function* stopped.\n"


def test_log_decorator_console_zero(capsys):
    """ Тест декоратора при делении на ноль. """

    @log()
    def my_function(x: float, y: float) -> float:
        return x / y

    my_function(6, 0)
    captured = capsys.readouterr()
    assert captured.out == "*my_function* started.\n*my_function* error: division by zero. Inputs (6, 0), {}\n*my_function* stopped.\n"
