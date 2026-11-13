import pytest

from app.shipping import shipping_cost


@pytest.mark.parametrize("peso,esperado", [(0.5, 15.0), (1.0, 15.0), (3.0, 25.0), (20.0, 45.0)])
def test_shipping_cost(peso, esperado):
    assert shipping_cost(peso) == esperado


@pytest.mark.parametrize("peso", [0, -2, 21])
def test_shipping_cost_invalid(peso):
    with pytest.raises(ValueError):
        shipping_cost(peso)
