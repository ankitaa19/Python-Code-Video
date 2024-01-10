class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item]['quantity'] <= quantity:
                del self.items[item]
            else:
                self.items[item]['quantity'] -= quantity

    def calculate_total(self):
        total_price = sum(item_info['price'] * item_info['quantity'] for item_info in self.items.values())
        return total_price

# Example usage:
cart = ShoppingCart()

cart.add_item("Laptop", 1200, 2)
cart.add_item("Headphones", 100)
cart.add_item("Mouse", 20, 3)

print("Total price in the shopping cart:", cart.calculate_total())

cart.remove_item("Headphones")

print("Total price after removing headphones:", cart.calculate_total())