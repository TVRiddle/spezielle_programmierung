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
    customers = DAO.get_all_customers()
    return dumps(customers)


@app.route('/cars')
def get_all_cars():
    cars = DAO.get_all_cars()
    return dumps(cars)

@app.route('/cars/available')
def get_all_cars_available():
    cars = DAO.get_all_available_cars()
    return dumps(cars)


@app.route('/customer/<customer_id>/book/<car_id>', methods=["GET"])
def book_car(customer_id, car_id):
    if DAO.insert_booking(customer_id, car_id):
        return "true"
    else:
        return "false"


@app.route('/customer/<customer_id>/history')
def get_history(customer_id):
    result = DAO.get_history(customer_id)
    return dumps(result)


if __name__ == '__main__':
    # imports testData
    DAO.put_test_data_to_db()
    # Start webserver
    for i in range(100):
        try:
            app.run(host="0.0.0.0", port=4000 + i,
                    debug=True, use_reloader=False)
            break
        except OSError:
            pass
