import random
import os
import json
import datetime

from bson import ObjectId
from pymongo import MongoClient
from flask import jsonify
from Booking import Booking

MONGODB_HOST = 'mongodb://root:example@mongoDB:27017'

### DB zum debuggen
#MONGODB_HOST = 'mongodb://root:example@localhost:4444'

client = MongoClient(MONGODB_HOST)
db = client.RentMe

now = datetime.datetime.now()


# Json-Datei loswerden!
def putTestDataToDB():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "./resources", "sample_data.json")
    with open(json_url) as data:
        data = json.load(data)
        cars_import = data["cars"]
        customers_import = data["customers"]

        for car in cars_import:
            db.cars.insert_one(car)

        for customer in customers_import:
            cars = db.cars.find({})
            for car in cars:
                if isCarAvailable(car["_id"]):
                    new_booking = Booking(car["_id"], now, now + datetime.timedelta(random.randint(1, 100)))
                    bookings = [new_booking]
                    customer["booking"] = bookings
                    break
            db.customers.insert_one(customer)


def getAllCustomers():
    customers = db.customers.find({})
    for customer in customers:
        id = customer["_id"]
        customer["_id"] = id
    return list(db.customers.find({}))


def getAllCars():
    return list(db.cars.find({}))


def getHistory(customer_id):
    return list(db.bookings.find({"customer_id": ObjectId(customer_id)}))


def insertBooking(booking):
    db.bookings.insert_one(jsonify(booking))


def isCarAvailable(car_id):
    return db.bookings.count_documents({'car_id': car_id}) == 0
