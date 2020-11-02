import random
import os
import json
import datetime

from bson import ObjectId
from pymongo import MongoClient
from Booking import Booking
from BookingDTO import BookingDTO

MONGODB_HOST = 'mongodb://root:example@mongoDB:27017'
### DB zum debuggen
# MONGODB_HOST = 'mongodb://root:example@localhost:4444'

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
            id = db.customers.insert_one(customer).inserted_id
            for car in cars:
                if isCarAvailable(car["_id"]):
                    new_booking = Booking(car["_id"], id, now, now + datetime.timedelta(random.randint(1, 100)))
                    db.bookings.insert_one(new_booking.__dict__)
                    break


def getAllCustomers():
    customers = db.customers.find({})
    for customer in customers:
        id = customer["_id"]
        customer["_id"] = id
    return list(db.customers.find({}))


def getAllCars():
    return list(db.cars.find({}))


def getHistory(customer_id):
    bookings = db.bookings.find({"customer_id": ObjectId(customer_id)})
    bookingList = []
    for booking in bookings:
        print(booking)
        car_id = booking["car_id"]
        name = db.cars.find_one({"_id": ObjectId(car_id)})["name"]
        bookingList.append(BookingDTO(name, booking["start"].timestamp(), booking["end"].timestamp()).__dict__)
    return list(bookingList)


def insertBooking(booking):
    db.bookings.insert_one(booking.__dict__)


def isCarAvailable(car_id):
    return db.bookings.count_documents({'car_id': ObjectId(car_id)}) == 0


def getCarName(car_id):
    return db.cars.find_one({'_id': ObjectId(car_id)})["car_name"]