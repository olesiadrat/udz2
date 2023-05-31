import sqlite3 

class Database():
    def __init__(self):
        self.open_connection()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tOrders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT NOT NULL,
            truck TEXT NOT NULL,
            weight INTEGER NOT NULL,
            width INTEGER NOT NULL,
            height INTEGER NOT NULL)"""
                    ) # создаем таблицу с заказами
        self.close_connection()

    def close_connection(self):
        self.cur.close()
        self.conn.close()

    def open_connection(self):
        self.conn = sqlite3.connect('orders.db')
        self.cur = self.conn.cursor()

    def drop(self):
        self.open_connection()
        self.cur.execute('''Drop table tOrders''')
        self.conn.commit()
        self.close_connection()

    def add_orders(self, customer, truck, weight, width, height):
        self.open_connection()
        self.cur.execute('INSERT into tOrders (customer, truck, weight, width, height) VALUES(?, ?, ?, ?, ?)',
                          (customer, truck, weight, width, height)
                         )
        self.conn.commit()
        self.close_connection()

    def get_orders(self):
        self.open_connection()
        self.cur.execute('SELECT * from tOrders')
        a = self.cur.fetchall()
        self.close_connection()
        return a

x = Database()
x.add_orders('Дмитрий', 'Бычок', 2.5, 1.5, 1.8)
print(x.get_orders())