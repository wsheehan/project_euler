# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

year = 1900
month = 1
day = 1

def is_leap_year(year):
	if year % 400 == 0:
		return False
	elif year % 4 == 0:
		return True
	else:
		return False

def end_of_month(year, month, day):
	l31 = [1,3,5,7,8,10,12]
	l30 = [4,6,9,11]
	if month in l31 and day == 31:
		return True
	elif month in l30 and day == 30:
		return True
	elif month == 2:
		if is_leap_year(year) and day == 29:
			return True
		elif is_leap_year(year) != True and day == 28:
			return True
	else:
		return False

j = 1
sundays = 0
while j > 0:
	if year == 2000 and month == 12 and day == 31:
		break
	if month == 12 and day == 31:
		day = 1
		month = 1
		year += 1
	elif end_of_month(year, month, day):
		day = 1
		month += 1
	else:
		day += 1
	if year > 1900 and j % 7 == 0 and day == 1:
		sundays += 1
	j += 1

print (sundays)
