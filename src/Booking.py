import Car
import Customer


class Booking:

    # initialize Booking
    def __init__(self, car: Car, customer: Customer, start, end):
        # ToDo Momentan gilt der Name als ID
        self.car = car
        self.customer = customer
        self.start = start
        self.end = end
        self.car.is_booked = True  # set a car as booked

    # define string function
    def __str__(self):
        return "{} {} {} {}".format(self.car, self.customer, self.start, self.end)

    # mapping the Booking data in JSON format
    def to_json(self):
        return '{"booking": ' + self.car.to_json() + ', "customer": ' + self.customer.to_json() + ', "start": "' + self.start.strftime(
            "%m/%d/%Y, %H:%M:%S") + '", "end": "' + self.end.strftime("%m/%d/%Y, %H:%M:%S") + '"}'
