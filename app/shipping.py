"""Calculo de frete por faixa de peso."""

FAIXAS = [(1.0, 15.0), (5.0, 25.0), (20.0, 45.0)]


def shipping_cost(weight_kg: float) -> float:
    """Retorna o frete para o peso informado, em kg."""
    if weight_kg <= 0:
        raise ValueError("peso deve ser positivo")
    for limite, valor in FAIXAS:
        if weight_kg <= limite:
            return valor
    raise ValueError("peso acima do limite de 20 kg")
