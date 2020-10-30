from pymongo import MongoClient

# Das stimmt nur so halb... wenn man mit python von außen zugreifen möchte. In der Dockerumgebung muss dies
# wahrscheinlich angepasst werden. Der standard port von MongoDB ist 27017. Host müsste der name des DockerContainers
# sein. Also "mongo"
MONGODB_HOST = 'mongodb://root:example@localhost:4444'
DB_NAME = 'RentMe'
CAR_COLLECTION = 'cars'
CUSTOMER_COLLECTION = 'customers'

client = MongoClient(MONGODB_HOST)
db = client[DB_NAME]



def getAllCustomers():
    collection = db[CUSTOMER_COLLECTION]
    allCustomers = collection.find({})
    for customer in allCustomers:
        print(customer)
