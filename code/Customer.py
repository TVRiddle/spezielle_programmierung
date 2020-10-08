import json


class Customer:
    def __init__(self, fist_name, last_name):
        self.first_name = fist_name
        self.last_name = last_name

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def to_json(self):
        return json.dumps(self.__dict__)
