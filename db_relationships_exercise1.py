from database import DatabaseContextManager

# ------------------------Table Creation------------------------


def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    amount_spent DECIMAL(10,2) DEFAULT 0.00)
    """
    with DatabaseContextManager("orders") as db:
        db.execute(query)


def create_table_products():
    query = """CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price DECIMAL(10,2),
    description TEXT)"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)


def create_table_orders():
    query = """CREATE TABLE IF NOT EXISTS Orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(id),
    FOREIGN KEY (product_id) REFERENCES Companies(id))"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)

# ------------------------Customers CRUD------------------------


def create_customer(first_name: str, last_name: str):
    query = """INSERT INTO Customers(first_name, last_name) VALUES(?, ?)"""
    parameters = [first_name, last_name]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_customers_name(customer_id: int, new_first_name: str, new_last_name: str):
    query = """UPDATE Customers
                SET first_name = ?, last_name = ?
                WHERE id = ?"""
    parameters = [new_first_name, new_last_name, customer_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def update_customers_amount_spent(customer_id: int, new_amount_spent: int):
    query = """UPDATE Customers
                SET amount_spent = ?
                WHERE id = ?"""
    parameters = [new_amount_spent, customer_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def delete_customer(customer_id: int):
    query = """DELETE FROM Customers
                WHERE id = ?"""
    parameters = [customer_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def get_customers_orders():
    query = """SELECT * FROM Customers
                JOIN Orders
                    ON Orders.customer_id = Customers.id"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


# def drop_customers_table():
#     query = """DROP TABLE Companies"""
#     with DatabaseContextManager("orders") as db:
#         db.execute(query)


# ------------------------Products CRUD------------------------


def create_product(name: str, price: int, description: str):
    query = """INSERT INTO Products(name, price, description) VALUES(?, ?, ?)"""
    parameters = [name, price, description]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def get_products():
    query = """SELECT * FROM Products"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_product_name(product_id: int, new_name: str):
    query = """UPDATE Products
                SET name = ?
                WHERE id = ?"""
    parameters = [new_name, product_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def update_product_price(product_id: int, new_price: int):
    query = """UPDATE Products
                SET price = ?
                WHERE id = ?"""
    parameters = [new_price, product_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def delete_product(product_id: int):
    query = """DELETE FROM Product
                WHERE id = ?"""
    parameters = [product_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def get_products_orders():
    query = """SELECT * FROM Products
                JOIN Companies
                    ON Customer.company_id = Companies.company_id"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


def drop_customers_table():
    query = """DROP TABLE Companies"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)


# ------------------------Orders CRUD------------------------

def create_order(customer_id: int, product_id: int):
    query = """INSERT INTO Orders(customer_id, product_id) VALUES(?, ?)"""
    parameters = [customer_id, product_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def get_orders():
    query = """SELECT * FROM Orders"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_order_product_id(order_id: int, new_product_id: int):
    query = """UPDATE Orders
                SET product_id = ?
                WHERE id = ?"""
    parameters = [new_product_id, order_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def update_order_customer_id(order_id: int, new_customer_id: int):
    query = """UPDATE Orders
                SET order_id = ?
                WHERE id = ?"""
    parameters = [new_customer_id, order_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def delete_order(order_id: int):
    query = """DELETE FROM Orders
                WHERE order_id = ?"""
    parameters = [order_id]
    with DatabaseContextManager("orders") as db:
        db.execute(query, parameters)


def get_orders_with_details():
    query = """SELECT * FROM Orders
                JOIN Products
                    ON Orders.product_id = Products.id
                JOIN Customers
                    ON Orders.customer_id = Customers.id"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


def drop_orders_table():
    query = """DROP TABLE Orders"""
    with DatabaseContextManager("orders") as db:
        db.execute(query)


# create_table_customers()
# create_table_orders()
# create_table_products()
#
# create_customer("Dalia", "Grybauskaite")
#
# create_product("kirvis", 25.99, "Geriausias kirvis mieste")

# create_order(1, 1)

# create_order(2, 2)
get_customers_orders()
# get_orders_with_details()
