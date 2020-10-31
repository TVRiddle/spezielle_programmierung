class BookingList(list):

    # initialize Booking list
    def __init__(self, bookings=None):
        if bookings == None:
            self.bookings = []
        else:
            self.bookings = bookings

    # add a booking into the list
    def addBooking(self, booking):
        for booking_list in self.bookings:
            if booking_list.car_name == booking.car_name:
                return False
        self.bookings.append(booking)
        return True

    def to_json(self):
        string = '{"BookingList": ['
        for booking in self.bookings:
            string = string + booking.to_json() + ","
        string = string[:-1]
        string = string + '"]}'
        return string
