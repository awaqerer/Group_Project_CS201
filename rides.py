total_revenue = 0


def calculate_cost(bike, minutes):
    return bike.get_price_per_minute() * minutes


def take_bike(client, station, bike_type=None):
    if client.current_bike is not None:
        return "already_has_bike"
    bike = station.take_bike(bike_type)
    if bike is None:
        return "no_bikes"
    client.current_bike = bike
    return "ok"


def return_bike(client, station, minutes):
    global total_revenue
    bike = client.current_bike
    if bike is None:
        return None
    cost = calculate_cost(bike, minutes)
    if not client.pay(cost):
        return None
    station.add_bike(bike)
    client.current_bike = None
    total_revenue += cost
    return cost

def get_total_revenue():
    return total_revenue