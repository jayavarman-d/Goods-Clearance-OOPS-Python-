from dbconnection import DatabaseCon
import datetime


class Invoice(DatabaseCon):

    def generate_bill(self, user_id, total_price):

        query = 'INSERT INTO invoice(user_id,invoice_time,total_price) VALUES (?,?,?)'
        self.cursor.execute(query, (user_id, datetime.datetime.now(), total_price))
        self.conn.commit()

        print('Invoice generated')
