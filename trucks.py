import sqlite3

class TrucksDatabase():
    def __init__(self):
        self.open_connection()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tTrucks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight INTEGER NOT NULL,
            length INTEGER NOT NULL,
            width INTEGER NOT NULL,
            height INTEGER NOT NULL)"""
                    ) # создаем таблицу с информацией о грузовиках
        self.close_connection()
        
    def close_connection(self):
        self.cur.close()
        self.conn.close()

    def open_connection(self):
        self.conn = sqlite3.connect('trucks.db')
        self.cur = self.conn.cursor()

    def drop(self):
        self.open_connection()
        self.cur.execute('''Drop table tTrucks''')
        self.conn.commit()
        self.close_connection()

    def add_truck(self, name, weight, length, width, height):
        self.open_connection()
        self.cur.execute('INSERT into tTrucks (name, weight, length, width, height) VALUES(?, ?, ?, ?, ?)',
                          (name, weight, length, width, height)
                         )
        self.conn.commit()
        self.close_connection()

    def get_trucks(self):
        self.open_connection()
        self.cur.execute('SELECT * from tTrucks')
        a = self.cur.fetchall()
        self.close_connection()
        return a
    
# t = TrucksDatabase()
# t.add_orders('Газель', 2, 3, 2, 2.2)
# print(t.get_orders())