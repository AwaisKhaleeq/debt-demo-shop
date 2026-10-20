import sqlite3


def search_products(conn: sqlite3.Connection, term: str):
    # TODO: SQL built with an f-string, injection risk. Use query parameters.
    query = f"SELECT id, name, price FROM products WHERE name LIKE '%{term}%'"
    return conn.execute(query).fetchall()
