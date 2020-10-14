import json


class Customer:

    # initialize Customer
    def __init__(self, fist_name, last_name):
        self.first_name = fist_name
        self.last_name = last_name

    # define string function
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    # mapping the Car data in JSON format
    def to_json(self):
        return json.dumps(self.__dict__)
