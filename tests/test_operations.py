from app.operations import add


def test_add_two_positive_numbers():
    result = add(5, 3)
    assert result == 8
