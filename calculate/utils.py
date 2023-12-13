def get_international_price(weight: int, price_per_kilo: int) -> int:
    """
    weight: kg

    weight * price_per_kilo
    """

    return weight * price_per_kilo


def get_domestic_price(weight: int, price_per_kilo: int) -> int:
    # We assume that the domestic price is 10% cheaper than the international price

    """
    weight: kg

    (weight * price_per_kilo) - ((weight * price_per_kilo) * 10 / 100)
    """
    return (weight * price_per_kilo) - ((weight * price_per_kilo) * 10 / 100)
