from platform import processor


class Product:
    def __init__(self, name, price, quantity, active=True):
        if not name:
            raise ValueError("No empty name allowed")
        if price < 0:
            raise ValueError("Price must be greater than 0")
        if quantity < 0:
            raise ValueError("Quantity must be greater than 0")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

        if self.quantity == 0:
            self.active = False


    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be greater than 0")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        #purchase request must be larger than 0
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        #product must be active
        if not self.active:
            raise Exception("Product ist currently not available")

        # check if item is in stock
        if quantity > self.quantity:
            raise Exception("Product is out of stock")

        #price calculation & update stock
        total_price = quantity * self.price
        self.quantity -= quantity

        #deactivates product if quantity equal to 0
        if self.quantity == 0:
            self.deactivate()

        return total_price

