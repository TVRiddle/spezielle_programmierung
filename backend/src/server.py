from flask import Flask
from Booking import Booking

import datetime
import random
from bson.json_util import dumps

import DAO

app = Flask(__name__)

now = datetime.datetime.now()


@app.route('/customers')
def get_all_customers():
    customers = DAO.getAllCustomers()
    return dumps(customers)


@app.route('/cars')
def get_all_cars():
    cars = DAO.getAllCars()
    return dumps(cars)


@app.route('/customer/<customer_id>/book/<car_id>', methods=["GET"])
def book_car(customer_id, car_id):
    if DAO.isCarAvailable(car_id):
        new_booking = Booking(car_id, customer_id, now, now + datetime.timedelta(random.randint(1, 100)))
        DAO.insertBooking(new_booking)
        return "true"
    else:
        return "false"


@app.route('/customer/<customer_id>/history')
def get_history(customer_id):
    bookings = DAO.getHistory(customer_id)
    return dumps(bookings)


if __name__ == '__main__':
    # imports testData
    DAO.putTestDataToDB()
    # Start webserver
    for i in range(100):
        try:
            app.run(host="0.0.0.0", port=4000 + i,
                    debug=True, use_reloader=False)
            break
        except OSError:
            pass
