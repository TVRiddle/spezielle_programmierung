from pymongo import MongoClient
import os
import json
import jsonify from flask

# Das stimmt nur so halb... wenn man mit python von außen zugreifen möchte. In der Dockerumgebung muss dies
# wahrscheinlich angepasst werden. Der standard port von MongoDB ist 27017. Host müsste der name des DockerContainers
# sein. Also "mongo"
MONGODB_HOST = 'mongodb://root:example@localhost:4444'
client = MongoClient(MONGODB_HOST)
db = client.RentMe

# Json-Datei loswerden!
def putTestDataToDB():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "../resources", "car_data.json")
    with open(json_url) as data:
        data = json.load(data)
        cars_import = data["cars"]
        customers_import = data["customers"]

        for car in cars_import:
            db.cars.insert_one(car)

        for customer in customers_import:
            db.customers.insert_one(customer)

            car = db.cars.find({}).limit(3)

            new_booking = Booking(car.name, new_Customer.first_name, new_Customer.last_name, now,
                                  now + datetime.timedelta(random.randint(1, 100)))

            db.booking.insert_one(jsonify(new_booking))
            print(new_booking)
            car_assigned = booking_list.addBooking(new_booking)

def getAllCustomers():
    collection = db.customers

