class BookingList(list):

    def __init__(self, bookings=None):
        if bookings == None:
            self.bookings = []
        else:
            self.bookings = bookings;

    def addBooking(self, booking):
        for booking_list in self.bookings:
            if booking_list.car.name == booking.car.name:
                return False
        self.bookings.append(booking)
        return True
