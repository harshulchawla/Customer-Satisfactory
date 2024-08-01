import sqlite3

from database import create_table

DATABASE = 'customer_satisfaction.db'

def drop_and_create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS customer_satisfaction')
    create_table()
    conn.close()

if __name__ == "__main__":
    drop_and_create_table()