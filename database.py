import sqlite3

DATABASE = 'customer_satisfaction.db'

def create_table():
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE customer_satisfaction (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                age INTEGER,
                flight_distance INTEGER,
                inflight_entertainment INTEGER,
                baggage_handling INTEGER,
                cleanliness INTEGER,
                departure_delay INTEGER,
                arrival_delay INTEGER,
                gender INTEGER,
                customer_type INTEGER,
                travel_type INTEGER,
                class_type TEXT,
                Class_Eco INTEGER,
                Class_Eco_Plus INTEGER
            )
        ''')
        conn.commit()
        conn.close()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_table()
