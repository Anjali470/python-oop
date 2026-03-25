from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    @property
    def product_id(self):
        return self.__product_id
    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def quantity(self):
        return self.__quantity
    @abstractmethod
    def calculate_total(self):
        raise NotImplementedError

class Electronics(Product):
    gst = 1.18
    def __init__(self, product_id, name, price, quantity, warranty_period):
        super().__init__(product_id, name, price, quantity)
        self.__warranty_period = warranty_period
    @property
    def warranty_period(self):
        return self.__warranty_period
    def calculate_total(self):
        return round(self.price * Electronics.gst * self.quantity, 2)

class Clothing(Product):
    gst = 1.12
    def __init__(self, product_id, name, price, quantity, size, color):
        super().__init__(product_id, name, price, quantity)
        self.__size = size
        self.__color = color
    @property
    def size(self):
        return self.__size
    @property
    def color(self):
        return self.__color
    def calculate_total(self):
        return round(self.price * Clothing.gst * self.quantity, 2 )

class Grocery(Product):
    gst = 1.05
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.__expiry_date = expiry_date
    @property
    def expiry_date(self):
        return self.__expiry_date
    def calculate_total(self):
        return round(self.price * Grocery.gst * self.quantity, 2)
