import datetime  # Importa el módulo completo para que el mock funcione


class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def print_receipt(self, customer: any) -> float:
        # Usamos datetime.datetime.now() para que coincida con el mock del test
        now = datetime.datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {timestamp}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_products_cost = 0.0
        for item, quantity in customer.product_cart.items():
            price = self.products[item]
            cost = quantity * price
            total_products_cost += cost
            unit_name = f"{item}s" if quantity > 1 else item

            # Lógica para evitar el .0 si el número es entero
            printable_cost = int(cost) if cost == int(cost) else cost
            print(f"{quantity} {unit_name} for {printable_cost} dollars")

        # Aplicamos la misma lógica al total
        total_print = (int(total_products_cost) 
                       if total_products_cost == int(total_products_cost) 
                       else total_products_cost)
        print(f"Total cost is {total_print} dollars")
        print("See you again!")
        return total_products_cost
