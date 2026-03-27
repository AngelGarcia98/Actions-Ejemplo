# test_app.py
import pytest
from app import suma

# Prueba 1: Caso feliz (UH-001: Validación de datos correctos)
def test_suma_positivos():
    assert suma(2, 3) == 5

# Prueba 2: Caso de borde con negativos
def test_suma_negativos():
    assert suma(-1, 1) == 0

# Prueba 3: Caso de fallo intencional (¡Para probar el pipeline!)
@pytest.mark.xfail # Esperamos que falle si activas esto
def test_suma_error_intencional():
    assert suma(2, 2) == 5