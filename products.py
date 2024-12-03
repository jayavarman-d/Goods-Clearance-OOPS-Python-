from abc import ABC,abstractmethod


class Products:

    def __init__(self, product_id, product_name, quantity, price):

        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity = quantity
        self.__price = price

    def get_prod_id(self):
        return self.__product_id

    def set_prod_id(self, product_id):
        self.__product_id = product_id

    def get_prod_name(self):
        return self.__product_name

    def set_prod_name(self, product_name):
        self.__product_name = product_name

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    @abstractmethod
    def display_products(self):
       pass
