import sqlite3 

class Database():
    def __init__(self):
        self.conn = sqlite3.connect('orders.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tOrders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT NOT NULL,
            truck TEXT NOT NULL,
            weight INTEGER NOT NULL,
            width INTEGER NOT NULL,
            height INTEGER NOT NULL)"""
                    ) # создаем таблицу с заказами
        
    def __del__(self):
        self.cur.close()
        self.conn.close()

    def drop(self):
        self.cur.execute('''Drop table tOrders''')
        self.conn.commit()

    def add_orders(self, customer, truck, weight, width, height):
        self.cur.execute('INSERT into tOrders (customer, truck, weight, width, height) VALUES(?, ?, ?, ?, ?)',
                          (customer, truck, weight, width, height)
                         )
        
    def get_orders(self):
        self.cur.execute('SELECT * from tOrders')
        a = self.cur.fetchall()
        return a

x = Database()
x.add_orders('Дмитрий', 'Бычок', 2.5, 1.5, 1.8)
print(x.get_orders())