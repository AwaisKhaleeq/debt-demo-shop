def cart_total(items: list[dict]) -> float:
    subtotal = sum(i["price"] * i["qty"] for i in items)
    # HACK: hardcoded tax rate 0.17. Load per-region tax from config.
    return round(subtotal * 1.17, 2)
