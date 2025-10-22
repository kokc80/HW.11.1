import time
from functools import wraps
import time

def log(filename=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            log_message = ''
            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                log_message = (f'Функция: {func.__name__}\n'
                               f'Аргументы {args}\n' 
                               f'Результат: {result}\n'
                               f'Время выполнения: {time.time() - start_time}\n')
            except :
                log_message = f'Error: Ошибка в функции: {func.__name__}. Аргументы: {args}, {kwargs}\n'
            if filename:
                with open(filename, 'w') as f:
                    f.write(f'{log_message}\n')
            else:
                print({log_message})
        return inner
    return wrapper


@log()
def my_func_div(x, y):
    res_div = x/y
    return (res_div)

my_func_div(20,0)