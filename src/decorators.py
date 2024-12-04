from functools import wraps


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                start = f"Function *{func.__name__}* started.\n"
                result = func(*args, **kwargs)
                result = f"*{func.__name__}* ok. Result is: {result}\n"
            except ZeroDivisionError as err:
                result = f"*{func.__name__}* error: {err}. Inputs {args}, {kwargs}\n"
            stop = f"Function *{func.__name__}* stopped."
            total_str = start + result + stop
            if filename:
                with open(filename, "w") as f:
                    f.write(total_str)
                    return
            else:
                print(total_str)
                return

        return inner

    return wrapper


@log(filename="my_log_file.txt")
# @log()
def my_function(x: float, y: float) -> float:
    """ Функция возвращает результат деления x на y. """
    return x / y


my_function(10, 0)
