import datetime


class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def print_receipt(self, customer: any) -> None:
        now = datetime.datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {timestamp}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0.0
        for item, qty in customer.product_cart.items():
            price = self.products[item]
            cost = qty * price
            total_cost += cost
            unit = f"{item}s" if qty > 1 else item
            # Formateo estricto a 2 decimales
            print(f"{qty} {unit} for {cost:.2f} dollars")

        print(f"Total cost is {total_cost:.2f} dollars")
        print("See you again!")
