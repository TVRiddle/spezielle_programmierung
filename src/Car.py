import json


class Car:
    def __init__(self, name, color, number_of_seats, brand):
        self.name = name
        self.color = color
        self.number_of_seats = number_of_seats
        self.brand = brand

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.color, self.number_of_seats, self.brand)

    def to_json(self):
        return json.dumps(self.__dict__)
