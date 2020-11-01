from pymongo import MongoClient
import os
import json
from flask import jsonify

from Booking import Booking
import datetime
import random

# Das stimmt nur so halb... wenn man mit python von außen zugreifen möchte. In der Dockerumgebung muss dies
# wahrscheinlich angepasst werden. Der standard port von MongoDB ist 27017. Host müsste der name des DockerContainers
# sein. Also "mongo"
MONGODB_HOST = 'mongodb://root:example@localhost:4444'
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
            _id = db.customers.insert_one(customer).inserted_id

            cars = db.cars.find({}).limit(3)

            for car in cars:
                new_booking = Booking(car._id, _id, now,
                                  now + datetime.timedelta(random.randint(1, 100)))

                db.bookings.insert_one(jsonify(new_booking))

def getAllCustomers():
    return db.customers

def getAllCars():
    return db.cars

def getHistory(customer_id):
    return db.bookings.find({"customer_id": customer_id})

def insertBooking(booking):
    db.bookings.insert_one(jsonify(booking))

def isCarAvailable(car_id):
    return not db.bookings.find({'car_id':car_id}).count() > 0