import copy

from flask import Flask
from flask import jsonify
from Booking import Booking
import os

import json
import datetime
import random

import dao

app = Flask(__name__)

now = datetime.datetime.now()

@app.route('/customers')
def get_all_customers():
    customers = dao.getAllCustomers()
    return jsonify(customers)


@app.route('/cars')
def get_all_cars():
    cars = dao.getAllCars()
    return jsonify(cars)


@app.route('/customer/<customer_id>/book/<car_id>', methods=["GET"])
def book_car(customer_id, car_id):
    if(dao.isCarAvailable(car_id)):
        new_booking = Booking(car_id, customer_id, now,
                                    now + datetime.timedelta(random.randint(1, 100)))

        dao.insertBooking(new_booking)

        return "true"
    else:
        return "false"


@app.route('/customer/<customer_id>/history')
def get_history(customer_id):
    bookings = dao.getHistory(customer_id)
    return jsonify(bookings)


if __name__ == '__main__':
    # Start webserver
    for i in range(100):
        try:
            app.run(host="0.0.0.0", port=4000 + i,
                    debug=True, use_reloader=False)
            break
        except OSError:
            pass
