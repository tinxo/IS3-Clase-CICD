from functions.calculadora import suma
import pytest

def test_suma():
    assert suma(2,5) == 7

@pytest.mark.parametrize(
    "valor_a, valor_b, resultado", 
    [
        (2,3,5),
        (0,5,5),
        (None,5,None),
        ('2',5,7),
        (2,suma(2,2),6),
    ]
)
def test_varios_casos(valor_a, valor_b, resultado): 
    # El nombre de la función TIENE que empezar con TEST
    temp = suma(valor_a,valor_b)
    assert  temp == resultado