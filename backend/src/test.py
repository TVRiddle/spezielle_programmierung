import time, random, datetime

from Booking import Booking

print("Try to make new booking for customer: " + str(1) + " and car: " + str(2))
now = int(time.mktime(datetime.datetime.now().timetuple()))
new_booking = Booking(1, 2, now, now + random.randint(100000, 100000))
print(new_booking.__dict__)

# import datetime, time
# dt = datetime.datetime(2011, 10, 21, 0, 0)
# s = int(time.mktime(dt.timetuple()))
# print(s)