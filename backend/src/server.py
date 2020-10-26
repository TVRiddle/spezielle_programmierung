import copy

from flask import Flask
from flask import jsonify
from Booking import Booking
from BookingList import BookingList
from Car import Car
from Customer import Customer
import os

import json
import datetime
import random

app = Flask(__name__)

customers = []
booking_list = BookingList()
cars = []
data_have_to_be_loaded = True

now = datetime.datetime.now()


def load_json():
    if (len(cars) == 0):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "resources", "car_data.json")
        with open(json_url) as data:
            data = json.load(data)
            cars_import = data["cars"]
            customers_import = data["customers"]

            for car in cars_import:
                new_car = Car(car["name"], car["color"],
                              car["number_of_seats"], car["brand"])
                cars.append(new_car)

            for customer in customers_import:
                new_Customer = Customer(
                    customer["first_name"], customer["last_name"])
                customers.append(new_Customer)
                car_assigned = False
                while not car_assigned:
                    car = cars[random.randint(0, len(cars) - 1)]
                    car.is_booked = True
                    new_booking = Booking(car.name, new_Customer.first_name, new_Customer.last_name, now,
                                          now + datetime.timedelta(random.randint(1, 100)))
                    print(new_booking)
                    car_assigned = booking_list.addBooking(new_booking)
    return "Done"


@app.route('/customers')
def get_all_customers():
    load_json()
    return jsonify([customer.__dict__ for customer in customers])


@app.route('/cars')
def get_all_cars():
    load_json()
    return jsonify([car.__dict__ for car in cars])


@app.route('/customer/<first_name>/<last_name>/book/<car_id>', methods=["GET"])
def book_car(first_name, last_name, car_id):
    load_json()
    for car in cars:
        if car.name == car_id:
            car_assigned = booking_list.addBooking(
                Booking(car.name, first_name, last_name, now, now + datetime.timedelta(random.randint(1, 100))))
            car.is_booked = True
            break
    if not car_assigned:
        return "Auto bereits gebucht."
    return "Auto wurde gebucht."


@app.route('/customer/<first_name>/<last_name>/history')
def get_history(first_name, last_name):
    load_json()
    found_bookings = []
    for booking in booking_list.bookings:
        if first_name == booking.customer_first_name and last_name == booking.customer_last_name:
            found_bookings.append(copy.deepcopy(booking))

    return jsonify([booking.__dict__ for booking in found_bookings])


if __name__ == '__main__':
    # Start webserver
    for i in range(100):
        try:
            app.run(host="0.0.0.0", port=4000 + i,
                    debug=True, use_reloader=False)
            break
        except OSError:
            pass
