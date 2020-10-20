from database import DatabaseContextManager

# ------------------------Table Creation------------------------


def create_table_customer():
    query = """CREATE TABLE IF NOT EXISTS Customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES Companies(company_id))
    """
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count INTEGER)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

# ------------------------Company CRUD------------------------


def create_company(company_name: str, employee_count: str):
    query = """INSERT INTO Companies(company_name, employee_count) VALUES(?, ?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_company_name(old_company_name: str, new_company_name: str):
    query = """UPDATE Companies
                SET company_name = ?
                WHERE company_name = ?"""
    parameters = [new_company_name, old_company_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_company(company_name: str):
    query = """DELETE FROM Companies
                WHERE company_name = ?"""
    parameters = [company_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customers_companies():
    query = """SELECT * FROM Customer
                JOIN Companies
                    ON Customer.company_id = Companies.company_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


def drop_companies_table():
    query = """DROP TABLE Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


# ------------------------Customer CRUD------------------------

def create_customer(first_name: str, last_name: str, age: int, company_id: int):
    query = """INSERT INTO Customer(first_name, last_name, age, company_id) VALUES(?,?,?,?)"""
    parameters = [first_name, last_name, age, company_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_customer(first_name: str, last_name: str):
    query = """DELETE FROM Customer
                WHERE first_name = ? AND last_name = ?"""
    parameters = [first_name, last_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customers():
    query = """SELECT * FROM Customer"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def get_customer(first_name: str, last_name: str):
    query = """SELECT * FROM Customer
                JOIN Companies
                    ON Customer.company_id = Company.company_id
                WHERE first_name = ? AND last_name = ?"""
    parameters = [first_name, last_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
        for record in db.fetchall():
            print(record)


def update_customer_age(first_name: str, last_name: str, new_age: int):
    query = """UPDATE Customer
                SET age = ?
                WHERE first_name = ? AND last_name = ?"""
    parameters = [new_age, first_name, last_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


# Table = "Customer"
# Fields = [first_name, last_name, age]


create_table_customer()
create_table_companies()

# create_company("Maxima", 1000)
# create_company("Iki", 500)

# create_customer("Darius", "Alekma", 25, 1)
# create_customer("Rokas", "Kilinskas", 15, 1)
# create_customer("Jonas", "Petrauskas", 45, 2)
# create_customer("testas", "testauskas", 5, 3)

print("================ Customers ================")
get_customers()
print("\n\n================ Companies ================")
get_companies()
print("\n\n================ Customers companies ================")
get_customers_companies()