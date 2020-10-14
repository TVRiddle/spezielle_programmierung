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
            if booking_list.car.name == booking.car.name:
                return False
        self.bookings.append(booking)
        return True
