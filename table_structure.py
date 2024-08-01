import sqlite3

DATABASE = 'customer_satisfaction.db'

def column_exists(cursor, table_name, column_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    return any(column_name == col[1] for col in columns)

def alter_table():
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        
        # Check if the column already exists
        if not column_exists(c, 'customer_satisfaction', 'travel_type'):
            # Add the missing column
            c.execute('ALTER TABLE customer_satisfaction ADD COLUMN travel_type INTEGER')
            conn.commit()
            print("Table altered successfully.")
        else:
            print("Column 'travel_type' already exists.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    alter_table()
