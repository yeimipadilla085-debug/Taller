def calculate_subtotal(
    unit_price: float,
    quantity: int,
) -> float:
    return unit_price * quantity


def calculate_tax(
    subtotal: float,
    tax_percentage: float,
) -> float:
    return subtotal * tax_percentage / 100


def calculate_invoice_total(
    unit_price: float,
    quantity: int,
    tax_percentage: float,
) -> float:
    subtotal = calculate_subtotal(unit_price, quantity)
    tax = calculate_tax(subtotal, tax_percentage)
    return subtotal + tax
