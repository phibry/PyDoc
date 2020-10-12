import datetime

t = datetime.time(5, 25, 1)
print(t)

print(t.hour)

# time
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

# dates
# calender date values
# year month and day
# today class method
today = datetime.date.today()
print(today)
print(today.timetuple())
print(today.year)  # year
print(today.month)
print(today.day)

# minimum
print(datetime.date.max)
print(datetime.date.min)


# replace
d1 = datetime.date(2015, 3, 11)  # yyyy mm, dd
print(d1)

d2 = d1.replace(year=1990)
print(d2)

# arithmic on datetime objects
print(d1-d2) # timedelta