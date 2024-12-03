from dbconnection import DatabaseCon
import datetime


class Invoice(DatabaseCon):

    def generate_bill(self, user_id, total_price):

        query = 'INSERT INTO invoice(user_id,invoice_time,total_price) VALUES (?,?,?)'
        self.cursor.execute(query, (user_id, datetime.datetime.now(), total_price))
        self.conn.commit()

        print('Invoice generated')

    def bill_details(self,user_id):

        bill_query = 'SELECT * FROM invoice WHERE user_id = ?'
        self.cursor.execute(bill_query, (user_id))
        bill = self.cursor.fetchall()

        for bill_id in range(len(bill)):
            bill[bill_id] =( bill[bill_id][0], bill[bill_id][1], bill[bill_id][2].strftime('%Y-%m-%d'), bill[bill_id][3] )
        return bill
