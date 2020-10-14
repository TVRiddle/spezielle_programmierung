import json
import datetime
import random

from Booking import Booking
from BookingList import BookingList
from Car import Car
from Customer import Customer

path = "../resouces/car_data.json"

customers = []
booking_list = BookingList()
cars = []

now = datetime.datetime.now()


def main():
    with open(path) as data:
        data = json.load(data)
        cars_import = data["data"]["cars"]
        customers_import = data["customers"]

        for car in cars_import:
            new_car = Car(car["name"], car["color"], car["number_of_seats"], car["brand"])
            cars.append(new_car)

        for customer in customers_import:
            new_Customer = Customer(customer["first_name"], customer["last_name"])
            customers.append(new_Customer)
            car_assigned = False
            while not car_assigned:
                car = cars[random.randint(0, len(cars) - 1)]
                car_assigned = booking_list.addBooking(
                    Booking(car, new_Customer, now, now + datetime.timedelta(random.randint(1, 100))))

    for car in cars:
        print(car.to_json())
    for customer in customers:
        print(customer.to_json())
    for booking in booking_list.bookings:
        print(booking.to_json())


main()
