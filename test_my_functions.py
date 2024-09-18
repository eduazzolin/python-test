import pytest
import my_functions


def test_add():
    """
    Testa se a função está retornando 5 quando 1 e 4 são
    passados como argumentos
    """
    result = my_functions.add(1, 4)
    assert result == 5


def test_add_strings():
    """
    Testa se a função lança uma exceção TypeError quando
    passamos strings como argumentos
    """
    result = my_functions.add("Nome ", "Sobrenome")
    assert result == "Nome Sobrenome"


def test_divide():
    """
    Testa se a função está retornando 4 quando 8 e 2 são
    passados como argumentos
    """
    result = my_functions.divide(8, 2)
    assert result == 4


def test_divide_by_zero():
    """
    Testa se a função lança uma exceção ZeroDivisionError
    quando o segundo argumento é 0
    """
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(8, 0)
