import sqlite3 as sql


class Database:
    def __init__(self, path):
        self.path = path
        self.con = sql.connect(path)

    def create_table(self):
        with self.con:
            self.con.execute('''
                CREATE TABLE IF NOT EXISTS Employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lastname TEXT NOT NULL,
                name TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
                )
                ''')
            self.con.execute('''
                CREATE TABLE IF NOT EXISTS Goods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_goods TEXT NOT NULL,
                article_goods INTEGER NOT NULL,
                about_goods TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
                )
                ''')
            self.con.execute('''
                CREATE TABLE IF NOT EXISTS Goods_date (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receipt_date TEXT NOT NULL,
                expiration_date TEXT NOT NULL,
                count_goods INTEGER NOT NULL,
                provider TEXT NOT NULL,
                id_goods INTEGER NOT NULL,
                FOREIGN KEY (id_goods) REFERENCES Goods (id)
                )
                ''')
            self.con.execute('''
                CREATE TABLE IF NOT EXISTS Store (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_store TEXT NOT NULL,
                address TEXT NOT NULL,
                x_coordinate REAL NOT NULL,
                y_coordinate REAL NOT NULL,
                id_good_date INTEGER NOT NULL,
                FOREIGN KEY (id_good_date) REFERENCES Goods_date (id)
                )
                ''')
            self.con.execute('''
                CREATE TABLE IF NOT EXISTS Cart (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                count INTEGER NOT NULL,
                id_goods INTEGER NOT NULL,
                FOREIGN KEY (id_goods) REFERENCES Goods (id)
                )
                ''')
            self.con.execute('''
                CREATE TABLE IF NOT EXISTS "Order"(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                process TEXT NOT NULL,
                date_order TEXT NOT NULL,
                id_client INTEGER NOT NULL,
                id_employee TEXT NOT NULL,
                id_cart INTEGER NOT NULL,
                FOREIGN KEY (id_client) REFERENCES Client (id),
                FOREIGN KEY (id_employee) REFERENCES Employee (id),
                FOREIGN KEY (id_cart) REFERENCES Cart (id)
                )
                ''')
            self.con.execute('''
                CREATE TABLE IF NOT EXISTS Client (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lastname TEXT NOT NULL,
                name TEXT NOT NULL,
                phone_number INTEGER NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                id_order INTEGER NOT NULL,
                FOREIGN KEY (id_order) REFERENCES "Order" (id)
                )
                ''')


db = Database('my_database.db')
db.create_table()
