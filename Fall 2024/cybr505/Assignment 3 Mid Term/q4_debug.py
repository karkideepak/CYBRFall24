class Item:
    def __init__(self, name, price, quantity, on_sale: bool=False):
        # setting the on sale value to false by defult make it clear
        if price < 0 or quantity < 0:
            raise ValueError ("Price & Quantity should be non negative")
        # adding edge case handling
        self.name = name
        self.price = price
        self.quantity = quantity
        self.on_sale = on_sale

def calculate_total(cart):
    if not cart:
        return 0.0
    # immediately return zero if the cart list is empty
    total = 0
    for item in cart:
        if item.on_sale:
            total += item.price * item.quantity * 0.9
        else:
            total += item.price * item.quantity
    return total

# Example usage
cart = [
    Item("Laptop", 1000, 1),
    Item("Mouse", 50, 2, True),
    Item("Keyboard", 80, 1, True)
]
print(f"Total price: ${calculate_total(cart):.2f}")
#print("Total price:", calculate_total(cart))
