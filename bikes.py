class Bike:
    def __init__(self, number):
        self.number = number

    def get_price_per_minute(self):
        return 2

    def get_kind(self):
        return "звичайний"


class ElectricBike(Bike):
    def get_price_per_minute(self):
        return 5

    def get_kind(self):
        return "електричний"


class Station:
    def __init__(self, name):
        self.name = name
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def take_bike(self, bike_type=None):
        for bike in self.bikes:
            if bike_type is None or type(bike) is bike_type:
                self.bikes.remove(bike)
                return bike
        return None

    def count_bikes(self):
        return len(self.bikes)