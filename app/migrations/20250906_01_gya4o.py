""" """

from yoyo import step

__depends__ = {}


def apply_step(conn):
    cursor = conn.cursor()
    with open("./src/items/infrastructure/item.sql") as f:
        item_sql = f.read()
    cursor.execute(item_sql)


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE items;")
    cursor.execute("DROP TRIGGER IF EXISTS items_timestamp_trigger ON items;")


steps = [step(apply_step, rollback_step)]
