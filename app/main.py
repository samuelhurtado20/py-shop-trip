import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "../config.json")
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
            message = (f"{customer.name}'s trip to the {shop.name} "
                       f"costs {round(cost, 2)}")
            print(message)
            if cost < min_cost:
                min_cost = cost
                cheapest_shop = shop

        if cheapest_shop and min_cost <= customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            cheapest_shop.print_receipt(customer)
            customer.money -= min_cost
            customer.location = cheapest_shop.location

            print(f"\n{customer.name} rides home")
            # Dividimos la línea para no exceder los 79 caracteres
            final_money = round(customer.money, 2)
            print(f"{customer.name} now has {final_money} dollars\n")
        else:
            msg = (f"{customer.name} doesn't have enough money "
                   "to make a purchase in any shop\n")
            print(msg)
