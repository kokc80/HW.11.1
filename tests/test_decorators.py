from src.decorators import *


def test_log_file(capsys):
    @log()
    def my_function(x, y) -> float:
        return x / y

    my_function(20, 0)
    result = capsys.readouterr()
    assert result.out == "Ошибка в функции: my_function Ошибка: division by zero. Аргументы: (20, 0), {}\n"
