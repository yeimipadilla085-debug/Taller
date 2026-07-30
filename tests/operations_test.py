from app.operations import subtract


def test_subtract_two_numbers():
    result = subtract(10, 4)
    assert result == 6
