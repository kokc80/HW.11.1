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
                log_message = (f'''Функция: {func.__name__}
                               Аргументы {args}
                               Результат: {resut}
                               Время выполнения: {time.time() - start_time}''')
            except Exception as e:
                error_message = (f'Ошибка в функции: {func.__name__} '
                                 f'Ошибка: {e}. Аргументы: {args}, {kwargs}')
                log_message = (f'{error_message}')
            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f'{log_message}\n')
            else:
                print({log_message})
        return inner
    return wrapper


@log('logs.txt')
def my_func_div(x, y):
    res_div = x/y
    return (res_div)

my_func_div(20,40)