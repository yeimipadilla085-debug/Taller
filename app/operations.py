def add(number_a: float, number_b: float) -> float:
    return number_a + number_b


def subtract(number_a: float, number_b: float) -> float:
    return number_a - number_b


def multiply(number_a: float, number_b: float) -> float:
    return number_a * number_b


def divide(number_a: float, number_b: float) -> float:
    if number_b == 0:
        raise ValueError("No es posible dividir entre cero")
    return number_a / number_b
