import json
import os
import datetime
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    # Resolución de ruta robusta para localizar config.json en /app/
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")

    # Fallback por si el entorno de ejecución mueve el archivo a la raíz
    if not os.path.exists(config_path):
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))
        config_path = os.path.join(root_dir, "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(c) for c in config["customers"]]
    shops = [Shop(s) for s in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        min_cost = float("inf")

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            # Redondeamos para el mensaje de log intermedio
            cost_print = round(cost, 2)
            # Si el costo termina en .0, lo tratamos como entero para el test
            if cost_print == int(cost_print):
                cost_print = int(cost_print)

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {cost_print}")

            if cost < min_cost:
                min_cost = cost
                cheapest_shop = shop

        if cheapest_shop and min_cost <= customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")

            # El método print_receipt ya maneja el Mock de datetime
            cheapest_shop.print_receipt(customer)

            # Actualizamos estado del cliente
            customer.money -= min_cost
            customer.location = cheapest_shop.location

            print(f"\n{customer.name} rides home")

            # Formateo de dinero final para evitar .0 innecesarios
            final_money = round(customer.money, 2)
            if final_money == int(final_money):
                final_money = int(final_money)
            print(f"{customer.name} now has {final_money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  "to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
