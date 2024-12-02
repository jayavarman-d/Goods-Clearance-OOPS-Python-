from invoice import Invoice
from dbconnection import DatabaseCon


class User(DatabaseCon):

    def display_products(self):

        query = 'SELECT * FROM products'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def buy(self, user_id, product_name, quantity):

        buy_query = 'SELECT * FROM products WHERE product_name= ?'
        self.cursor.execute(buy_query,(product_name,))
        prod = self.cursor.fetchone()

        if prod and prod[3] >= quantity:
            total_price = quantity * prod[2]

            update_query = 'UPDATE products SET available_stock=available_stock - ? WHERE product_name= ?'
            self.cursor.execute(update_query, (quantity, product_name))
            self.conn.commit()

            invoice = Invoice()
            invoice.generate_bill(user_id, total_price)

            print(f'Purchased Successfully!!! Total Amount: {total_price}')
        else:
            print('Insufficient Stock or product Not Found!!!')
