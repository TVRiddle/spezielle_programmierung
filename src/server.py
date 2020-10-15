from flask import Flask
from flask import request
from Booking import Booking
from BookingList import BookingList
from Car import Car
from Customer import Customer

import json
import datetime
import random

app = Flask(__name__)

path = "../resouces/car_data.json"

customers = []
booking_list = BookingList()
cars = []

now = datetime.datetime.now()

def load_json():
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

# Larissa
@app.route('/customers')
def get_all_customers():
    return 'Hello, World!'

# Larissa
@app.route('/cars')
def get_all_cars():
    return 'Hello, World!'

@app.route('/customer/<first_name>/<last_name>/book/', methods=["POST"])
def book_car(first_name, last_name):
    payload = request.get_json()
    car_id = payload["card_id"]
    car_assigned = booking_list.addBooking(Booking(car_id, Customer(first_name, last_name), now, now + datetime.timedelta(random.randint(1, 100))))
    if not car_assigned:
        return 406
    return 200

@app.route('/customer/<first_name>/<last_name>/history')
def get_history(first_name, last_name):
    found_bookings = BookingList()
    for booking in booking_list:
        if (first_name == booking.customer.first_name and last_name == booking.customer.last_name):
            found_bookings.append(booking)
    return found_bookings

if __name__ == '__main__':
    # Start webserver
    for i in range(100):
        try:
            app.run(host="0.0.0.0", port=8080 + i, debug=True)
            load_json()
            break
        except OSError:
            pass
