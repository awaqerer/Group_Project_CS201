from bikes import Bike, ElectricBike, Station
from Clients import Client
from rides import take_bike, return_bike, get_total_revenue


def make_ride(client, from_station, to_station, minutes, bike_type=None):
    # проводить поїздку і повертає текст результату (сама нічого не друкує)
    status = take_bike(client, from_station, bike_type)
    if status == "no_bikes":
        return f"{from_station.name}: велосипедів немає"
    if status == "already_has_bike":
        return f"{client.name} вже катається"

    bike = client.current_bike
    cost = return_bike(client, to_station, minutes)
    if cost is None:
        return f"{client.name}: не вистачає грошей"
    return f"{client.name}: {from_station.name} -> {to_station.name}, {minutes} хв, {cost} грн"

def print_report(stations):
    # друкує звіт адміністратора
    print("Звіт:")
    for station in stations:
        print(f"{station.name} — велосипедів: {station.count_bikes()}")
    print(f"Виручка: {get_total_revenue()} грн")



def main():
    # 1. Станції
    central = Station("Центральна")
    railway = Station("Вокзальна")

    # 2. Велосипеди
    central.add_bike(Bike(1))
    central.add_bike(Bike(2))
    central.add_bike(ElectricBike(3))
    railway.add_bike(ElectricBike(4))

    # 3. Клієнти
    olya = Client("Оля", 300)
    petro = Client("Петро", 100)

    # 4. Поїздки
    print("Поїздки:")
    print(make_ride(olya, central, railway, 20, bike_type=ElectricBike))
    print(make_ride(petro, central, railway, 15))
    print(make_ride(olya, central, railway, 25))

    # 5. Спроба взяти велосипед на порожній станції
    print("\nПорожня станція:")
    print(make_ride(petro, central, railway, 10))

    # 6. Баланси
    print("\nБаланси:")
    for client in [olya, petro]:
        print(f"{client.name}: {client.balance} грн")

    # 7. Звіт
    print()
    print_report([central, railway])

    # 8. Перевірки
    assert Bike(99).get_price_per_minute() == 2
    assert ElectricBike(98).get_price_per_minute() == 5
    assert central.count_bikes() == 0
    assert railway.count_bikes() == 4
    assert olya.balance == 150
    assert get_total_revenue() == 180
    print("\nВсе працює")


if __name__ == "__main__":
    main()
