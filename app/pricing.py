"""Calculos de preco de um carrinho de compras."""


def apply_discount(price: float, percent: float) -> float:
    """Aplica um desconto percentual (0-100) ao preco."""
    if price < 0:
        raise ValueError("preco nao pode ser negativo")
    if not 0 <= percent <= 100:
        raise ValueError("desconto deve estar entre 0 e 100")
    return round(price * (1 - percent / 100), 2)


def cart_total(items: list[dict]) -> float:
    """Soma preco * quantidade dos itens do carrinho."""
    total = 0.0
    for item in items:
        total += item["price"] * item.get("qty", 1)
    return round(total, 2)
