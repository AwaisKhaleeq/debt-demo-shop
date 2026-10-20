from datetime import datetime


def parse_order_date(value: str) -> datetime:
    # TODO: duplicated date parsing, same logic as parse_ship_date. Extract a helper.
    return datetime.strptime(value.strip(), "%Y-%m-%d")


def parse_ship_date(value: str) -> datetime:
    return datetime.strptime(value.strip(), "%Y-%m-%d")
