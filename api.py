from cart import cart_total


def checkout(request: dict) -> dict:
    # TODO: no tests for the checkout endpoint. Add happy-path and empty-cart tests.
    total = cart_total(request.get("items", []))
    return {"status": "ok", "total": total}
