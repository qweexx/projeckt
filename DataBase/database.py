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

    def get_data(self,table, name_table, data):
        for item in data[name_table]:
            self.con.execute(table, item)

    def fill_table(self, data):
        sql_insert_employee ="INSERT OR IGNORE INTO Employee (lastname, name, username, password) values(?, ?, ?, ?)"
        sql_insert_goods ="INSERT OR IGNORE INTO Goods (name_goods, article_goods, about_goods, category, price) values(?, ?, ?, ?, ?)"
        sql_insert_goods_date ="INSERT OR IGNORE INTO Goods_date (receipt_date, expiration_date, count_goods, provider, id_goods) values(?, ?, ?, ?, ?)"
        sql_insert_store ="INSERT OR IGNORE INTO Store (name_store, address, x_coordinate, y_coordinate, id_good_date) values(?, ?, ?, ?, ?)"
        sql_insert_cart ="INSERT OR IGNORE INTO Cart (count, id_goods) values(?, ?)"
        sql_insert_order ="INSERT OR IGNORE INTO 'Order' (process, date_order, id_client, id_employee, id_cart) values(?, ?, ?, ?, ?)"
        sql_insert_client ="INSERT OR IGNORE INTO Client (lastname, name, phone_number, email, address, id_order) values(?, ?, ?, ?, ?, ?)"

        self.get_data(sql_insert_employee, 'employee', data)
        self.get_data(sql_insert_goods, 'goods', data)
        self.get_data(sql_insert_goods_date, 'goods_date', data)
        self.get_data(sql_insert_store, 'store', data)
        self.get_data(sql_insert_cart, 'cart', data)
        self.get_data(sql_insert_order, 'order', data)
        self.get_data(sql_insert_client, 'client', data)
        self.con.commit()

    def get_table_data(self, name_table):
        data = self.con.execute(f'''SELECT * FROM {name_table}''')
        data = data.fetchall()
        return data

    def get_username_password(self):
        data = self.con.execute('''SELECT username, password FROM Employee''')
        data = data.fetchall()
        return data


data = {
    'employee': [
        ('Smith', 'John', 'jsmith', 'password123'),
        ('Doe', 'Jane', 'jdoe', 'securepass')
    ],
    'goods': [
        ('Laptop', 'LP123', 'High-end laptop', 'Electronics', 1500.0),
        ('Smartphone', 'SP456', 'Latest smartphone', 'Electronics', 800.0)
    ],
    'goods_date': [
        ('2024-10-01', '2025-10-01', 50, 'TechProvider', 1),
        ('2024-09-15', '2025-09-15', 100, 'MobileSupplier', 2)
    ],
    'store': [
        ('Tech Store', '123 Tech Street', 40.712776, -74.005974, 1),
        ('Mobile Store', '456 Mobile Avenue', 34.052235, -118.243683, 2)
    ],
    'cart': [
        (2, 1),
        (3, 2)
    ],
    'order': [
        ('Processing', '2024-10-02', 1, 1, 1),
        ('Completed', '2024-09-30', 2, 2, 2)
    ],
    'client': [
        ('Williams', 'Michael', '123456789', 'michael@example.com', '789 Elm Street', 1),
        ('Brown', 'Emily', '987654321', 'emily@example.com', '321 Pine Avenue', 2)
    ]
}

db = Database('my_database.db')
# db.create_table()
# db.fill_table(data)
