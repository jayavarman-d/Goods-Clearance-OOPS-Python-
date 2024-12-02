from dbconnection import DatabaseCon


class Login(DatabaseCon):
    def __init__(self):
        super().__init__()
        self.__user_data = None

    def login(self, username, password):
        query = "SELECT * FROM users WHERE username= ? AND password = ?"
        self.cursor.execute(query, (username, password))
        self.__user_data = self.cursor.fetchone()
        if self.__user_data:
            print(f'Welcome {self.__user_data[1]}!')
            return self.__user_data
        else:
            print('Invalid Credentials')
            return None

    def signup(self, username, password, mobile, user_type):
        try:
            if len(mobile) == 10:
                raise Exception
            signup_query = 'INSERT INTO users(username,password,mobile_number,user_type) VALUES(?,?,?,?)'
            self.cursor.execute(signup_query, (username, password, mobile, user_type))
            self.conn.commit()
            print('Signup Successful!!!')
        except Exception as e:
            print('Invalid Values Mobile Number should be 10 digits')
        #   print(e)
        #   from main import Home
        #   call = Home.main_page()
