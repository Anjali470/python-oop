from abc import ABC, abstractmethod
from typing import List

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
    def __str__(self):
        return f"[Product ID: {self.product_id}] {self.name} Price: {self.price} Quantity: {self.quantity}"

class Electronics(Product):
    gst = 1.18
    def __init__(self, product_id, name, price, quantity, warranty_period):
        super().__init__(product_id, name, price, quantity)
        self.__warranty_period = warranty_period
    @property
    def warranty_period(self):
        return self.__warranty_period
    def calculate_total(self):
        return round(self.price * self.gst * self.quantity, 2)
    def __str__(self):
        return f"[Product ID: {self.product_id}] {self.name} Price: {self.price} Quantity: {self.quantity} [Warranty Period: {self.warranty_period}]"

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
        return round(self.price * self.gst * self.quantity, 2)
    def __str__(self):
        return f"[Product ID: {self.product_id}] {self.name} Price: {self.price} Quantity: {self.quantity} [Size: {self.size} Color: {self.color}]"

class Grocery(Product):
    gst = 1.05
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.__expiry_date = expiry_date
    @property
    def expiry_date(self):
        return self.__expiry_date
    def calculate_total(self):
        return round(self.price * self.gst * self.quantity, 2)
    def __str__(self):
        return f"[Product ID: {self.product_id}] {self.name} Price: {self.price} Quantity: {self.quantity} [Expiry Date: {self.expiry_date}]"

class ShoppingCart:
    def __init__(self):
        self.__products: List[Product] = []
        self.__discount_percentage = 0.0

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            return "Only Product instance can be added"
        self.__products.append(product)
        return f"Added {product.name} (id = {product.product_id}) to cart"

    def remove_product(self, product_id: int):
        for index, product in enumerate(self.__products):
            if product.product_id == product_id:
                removed = product
                self.__products.pop(index)
                return f"Removed {removed.name} (id = {removed.product_id}) from cart"
        return "Product not found"

    def calculate_cart_total(self):
        total = sum(product.calculate_total() for product in self.__products)
        return round(total, 2)

    def apply_discount(self, percentage):
        if  percentage < 0 or percentage > 100:
            return "Percentage is not valid"
        self.__discount_percentage = percentage
        return f"Applied discount: {percentage}"

    def checkout(self):
        sub_total = self.calculate_cart_total()
        discount_amount = round(sub_total * (self.__discount_percentage / 100), 2)
        total_payable = round(sub_total - discount_amount, 2)
        summary = {
            "items": [str(product) for product in self.__products],
            "sub_total": sub_total,
            "discount_percentage": self.__discount_percentage,
            "discount_amount": discount_amount,
            "total_amount": total_payable
        }
        self.__products.clear()
        self.__discount_percentage = 0.0
        return summary

    def display_cart(self):
        if not self.__products:
            print("Cart is empty")
            return
        print("==CART==")
        for product in self.__products:
            print("- ", product)
        print(f"Sub Total: {self.calculate_cart_total()}")
        if self.__discount_percentage:
            print(f"Discount: {self.__discount_percentage}%")

def main():
    # Create products
    laptop = Electronics(1, "Laptop", 50000, 1, "2 years")
    tshirt = Clothing(2, "T-Shirt", 1000, 2, "M", "Black")
    rice = Grocery(3, "Rice", 60, 5, "2026-12-31")

    # Create cart
    cart = ShoppingCart()

    print("\n--- Adding Products ---")
    print(cart.add_product(laptop))
    print(cart.add_product(tshirt))
    print(cart.add_product(rice))

    print("\n--- Display Cart ---")
    cart.display_cart()

    print("\n--- Calculate Total ---")
    print("Total:", cart.calculate_cart_total())

    print("\n--- Apply Discount ---")
    print(cart.apply_discount(10))  # 10% discount

    print("\n--- Cart After Discount ---")
    cart.display_cart()

    print("\n--- Remove Product ---")
    print(cart.remove_product(2))  # remove T-Shirt

    print("\n--- Cart After Removal ---")
    cart.display_cart()

    print("\n--- Checkout ---")
    summary = cart.checkout()

    print("\n--- Checkout Summary ---")
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\n--- Cart After Checkout ---")
    cart.display_cart()

if __name__ == "__main__":
    main()