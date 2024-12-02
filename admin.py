from dbconnection import DatabaseCon


class Admin(DatabaseCon):

    def display_products(self):

        query = 'SELECT * FROM products'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_prod(self, name, quantity, price):

        query = 'INSERT INTO products(product_name,available_quantity,price) VALUES(?,?,?)'
        self.cursor.execute(query)
        self.conn.commit()
        print("Product Added Successfully")

    def del_prod(self, prod_id):

        query = 'DELETE FROM products WHERE product_id=?'
        self.cursor.execute(query, (prod_id,))
        self.conn.commit()

        print('Product deleted Successfully!!!')