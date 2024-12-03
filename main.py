from login import Login
from admin import Admin
from user import User
from invoice import Invoice


class Home:
    def main_page(self):

        login_fun = Login()

        while True:
            print("\nWelcome to International Goods Clearance")
            print("1.Signup")
            print("2.Login")
            print("3.Exit")

            option = input("Enter Your Option")

            if option == '1':
                username = input('Enter Username')
                password = input('Enter Password')
                mobile = input('Enter Mobile Number')
                #user_type=input('Enter user type (default: user): ')
                user_type = 'user'
                login_fun.signup(username,password,mobile,user_type)

            elif option == '2':
                username = input('Enter username')
                password = input('Enter Password')

                user_val = login_fun.login(username,password)
                if user_val:
                    if user_val[4] == 'admin':
                        admin_fun = Admin()

                        while True:
                            print('\nAdmin Menu')
                            print('1.View Products')
                            print('2.Add Products')
                            print('3.Delete Product')
                            print('4.Logout')
                            admin_option = input('Enter your option')

                            if admin_option == '1':

                                for products in admin_fun.display_products():
                                    print(products)
                            #    break

                            elif admin_option == '2':

                                name = input('Enter Product name: ')
                                quantity = int(input('Enter Quantity: '))
                                price = int(input('Enter Price/Product'))

                                admin_fun.add_prod(name,quantity,price)

                            elif admin_option == '3':

                                prod_id = input('Enter Product ID: ')
                                admin_fun.del_prod(prod_id)

                            elif admin_option == '4':
                                break

                            else:
                                print('Invalid option Try Again')

                    elif user_val[4] == 'user':
                        user_fun = User()

                        while True:
                            print('\nUser Menu')
                            print('1.View Products')
                            print('2.Buy Products')
                            print('3.Bill Details')
                            print('4.Logout')

                            user_option = input('Enter your Option')

                            if user_option == '1':

                                for product in user_fun.display_products():
                                    print(product)

                            elif user_option == '2':

                                product_name = input('Enter Product name:')
                                quantity = int(input('Enter Quantity: '))

                                user_fun.buy(user_val[0],product_name,quantity)

                            elif user_option == '3':
                                print('\n Bill Details')

                                invoice_fun= Invoice()
                                for bill_id in invoice_fun.bill_details(user_val[0]):
                                    print(bill_id)

                            elif user_option == '4':
                                break

                            else:
                                print('Invalid option Try Again!!')

            elif option == '3':
                print('Exiting Application!! Thank You!!!')
                break
            else:
                print('Enter Valid Option!!!')

obj = Home()
obj.main_page()
