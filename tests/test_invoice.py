from app.invoice import calculate_subtotal, calculate_tax, calculate_invoice_total


def test_calculate_subtotal_returns_price_times_quantity():
    # Arrange
    unit_price = 25000
    quantity = 4

    # Act
    result = calculate_subtotal(unit_price, quantity)

    # Assert
    assert result == 100000


def test_calculate_tax_returns_percentage_of_subtotal():
    # Arrange
    subtotal = 100000
    tax_percentage = 19

    # Act
    result = calculate_tax(subtotal, tax_percentage)

    # Assert
    assert result == 19000


def test_calculate_invoice_total_returns_subtotal_plus_tax():
    # Arrange
    unit_price = 50000
    quantity = 2
    tax_percentage = 19

    # Act
    result = calculate_invoice_total(unit_price, quantity, tax_percentage)

    # Assert
    assert result == 119000
