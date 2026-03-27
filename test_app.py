import pytest
from app import suma

# Prueba 1: Caso feliz
def test_suma_positivos():
    assert suma(2, 3) == 5

# Prueba 2: Caso de borde
def test_suma_negativos():
    assert suma(-1, 1) == 0

# Prueba 3: Caso de fallo intencional (¡PEGADO AL DECORADOR!)

def test_suma_error_intencional():
    assert suma(2, 2) == 4