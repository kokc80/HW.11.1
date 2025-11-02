import time


def log(filename=None):
    '''Декоратор для логирования поведения функции'''
    def wrapper(func):
        def inner(*args, **kwargs):
            log_message = ''
            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                log_message = (f'Функция: {func.__name__} Результат: {result}')
            except Exception as e:
                error_message = (f'Ошибка в функции: {func.__name__} Ошибка: {e}.'
                                 f' Аргументы: {args}, {kwargs}')
                log_message = (f'{error_message}')
                log_message = log_message
            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f'{start_time} - {log_message}')
            else:
                print(log_message)
        return inner
    return wrapper


@log('mylog.txt')
def my_func_div(x, y) -> float:
    """Функция сложения x+y"""
    res_div = x + y
    return (res_div)


my_func_div(20, 0)
