from datetime import datetime


class Shop:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def print_receipt(self, customer) -> float:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {timestamp}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_products_cost = 0
        for item, quantity in customer.product_cart.items():
            price = self.products[item]
            cost = quantity * price
            total_products_cost += cost
            unit_name = f"{item}s" if quantity > 1 else item
            print(f"{quantity} {unit_name} for {cost} dollars")

        print(f"Total cost is {total_products_cost} dollars")
        print("See you again!")
        return total_products_cost
