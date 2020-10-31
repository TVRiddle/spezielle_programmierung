
class Booking:

    # initialize Booking
    def __init__(self, car_name, customer_first_name, customer_last_name, start, end):
        # ToDo Momentan gilt der Name als ID
        self.car_name = car_name
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name
        self.start = start
        self.end = end

    # define string function
    def __str__(self):
        return "{} {} {} {} {}".format(self.car_name, self.customer_first_name, self.customer_last_name, self.start,
                                       self.end)
