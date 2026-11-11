
class Bicycle:

    def __init__(self, number):
        self.number = number


class ElectricBicycle(Bicycle):

    def __init__(self, number):
        super().__init__(number)


class Station:

    def __init__(self, name):
        self.name = name
        self.bicycles = []

    def add_bicycle(self, bicycle):
        pass

    def remove_bicycle(self, bicycle_number):
        pass

    def get_bicycles(self):
        pass

    def count_bicycles(self):
        pass
