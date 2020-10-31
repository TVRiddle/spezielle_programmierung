import json


class Car:

    # initialize Car
    def __init__(self, name, color, number_of_seats, brand):
        self.name = name
        self.color = color
        self.number_of_seats = number_of_seats
        self.brand = brand
        self.is_booked = False

    # define string function
    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.color, self.number_of_seats, self.brand, self.is_booked)

    # mapping the Car data in JSON format
    def to_json(self):
        return json.dumps(self.__dict__)
