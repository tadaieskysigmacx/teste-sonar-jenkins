import pytest

from app.pricing import apply_discount, cart_total


def test_apply_discount():
    assert apply_discount(200.0, 10) == 180.0


def test_apply_discount_zero_and_full():
    assert apply_discount(50.0, 0) == 50.0
    assert apply_discount(50.0, 100) == 0.0


@pytest.mark.parametrize("price,percent", [(-1, 10), (10, -1), (10, 101)])
def test_apply_discount_invalid(price, percent):
    with pytest.raises(ValueError):
        apply_discount(price, percent)


def test_cart_total():
    items = [{"price": 10.0, "qty": 2}, {"price": 5.5}]
    assert cart_total(items) == 25.5


def test_cart_total_empty():
    assert cart_total([]) == 0.0
