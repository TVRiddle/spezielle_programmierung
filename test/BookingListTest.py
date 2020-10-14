import datetime

from Booking import Booking
from BookingList import BookingList
from Car import Car
from Customer import Customer

bookingList = BookingList()

car = Car("TestName", "TestColor", 0, "Testbrand")
customer = Customer("TestName", "TestName")
booking = Booking(car, customer, datetime.datetime.now(), datetime.datetime.now())
bookingList.addBooking(booking)

assert bookingList.addBooking(booking) == False
