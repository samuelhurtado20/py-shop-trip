import math


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = data["car"]

    def get_distance(self, target_location: list[int]) -> float:
        return math.sqrt(
            (self.location[0] - target_location[0]) ** 2
            + (self.location[1] - target_location[1]) ** 2
        )

    def calculate_trip_cost(self, shop: any, fuel_price: float) -> float:
        distance = self.get_distance(shop.location)
        fuel_needed = (distance * 2 * self.car["fuel_consumption"]) / 100
        fuel_cost = fuel_needed * fuel_price

        product_cost = sum(
            self.product_cart[item] * shop.products[item]
            for item in self.product_cart
        )
        return fuel_cost + product_cost
