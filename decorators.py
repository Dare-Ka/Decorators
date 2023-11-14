from functools import wraps
from datetime import datetime
import os


def logger_1(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'Время вызова:{datetime.now()}\n'
                       f'Имя функции:{old_function.__name__}\n'
                       f'Аргументы:{args}, {kwargs}\n'
                       f'Возвращаемое значение:{result}\n')
        return result

    return new_function


def logger_2(path):

    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(
                    f'Время вызова:{datetime.now()}\n'
                    f'Имя функции:{old_function.__name__}\n'
                    f'Аргументы:{args}, {kwargs}\n'
                    f'Возвращаемое значение:{result}\n')
            return result
        return new_function

    return __logger
