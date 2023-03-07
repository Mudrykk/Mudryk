import sqlite3


class Database():
    """This class is for working with the database."""

    def __init__(self):
        self.connection = sqlite3.connect(
            '/Users/User/Mudryk/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        """A method for returns the version of the database."""
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def create_user(self, customer_id, name, address, city, postalCode, country):
        """A method for creating a new user in the customers table."""
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES ({customer_id}, '{name}', '{address}', '{city}', {postalCode}, '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def get_all_users(self):
        """A method for selecting data from a database."""
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_user_address_by_name(self, name):
        """A method for selecting data from a database by name."""
        query = f"SELECT address, city, postalCode, country FROM \
            customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        """A method for updating data in a database."""
        query = f"UPDATE Products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_by_id(self, product_id):
        """A method for selecting data from table products by id."""
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def insert_product(self, product_id, name, description, qnt):
        """A method for inserting new data into a database."""
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        """A method for deleting data from a database."""
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        """A method for combining tables in a database."""
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                    JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record
