from app.operations import multiply


def comprobar_multiplicacion():
    result = multiply(4, 5)
    assert result == 20
