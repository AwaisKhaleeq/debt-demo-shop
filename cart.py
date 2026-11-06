DISCOUNT_CODES = {"WELCOME10": 0.10, "FRIENDS5": 0.05}


def cart_total(items: list[dict], code: str | None = None) -> float:
    subtotal = sum(i["price"] * i["qty"] for i in items)
    if code in DISCOUNT_CODES:
        subtotal *= 1 - DISCOUNT_CODES[code]
    # HACK: hardcoded tax rate 0.17. Load per-region tax from config.
    return round(subtotal * 1.17, 2)
