import json
import os
import datetime
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")
    if not os.path.exists(config_path):
        config_path = os.path.join(current_dir, "..", "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(c) for c in config["customers"]]
    shops = [Shop(s) for s in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money:.2f} dollars")

        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {cost:.2f}")

            if cost < min_trip_cost:
                min_trip_cost = cost
                cheapest_shop = shop

        if cheapest_shop and min_trip_cost <= customer.money:
            # 1. Guardar ubicación original (casa)
            home_location = customer.location

            # 2. Viajar a la tienda (actualizar ubicación)
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.location = cheapest_shop.location

            # 3. Pagar el viaje total y comprar
            customer.money -= min_trip_cost

            # 4. Imprimir recibo (mientras está en la tienda)
            cheapest_shop.print_receipt(customer)

            # 5. Regresar a casa (restaurar ubicación)
            customer.location = home_location
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  "to make a purchase in any shop\n")


if __name__ == "__main__":
    shop_trip()
