# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

def ldigit(n):
	x = n % 10
	if x == 1 or x == 2 or x == 6:
		return 3
	elif x == 3 or x == 7 or x == 8:
		return 5
	elif x == 4 or x == 5 or x == 9:
		return 4
	else:
		return 0

l = [6, 6, 5, 5, 7, 6, 6]
def sdigit(n):
	x = n % 100
	if x < 10:
		return ldigit(x)
	elif x == 10:
		return 3
	elif x > 10 and x < 20:
		if x == 11 or x == 12:
			return 6
		elif x == 13 or x == 14 or x == 19:
			return 8
		elif x == 15 or x == 16:
			return 7
		elif x == 17 or x == 18:
			return 9
	else:
		y = int(str(x)[:1])
		return y + ldigit(x%10)

def fdigit(n):
	y = int(str(n)[:1])
	if n >= 100:
		return 10 + ldigit(y)
	else:
		return ldigit(y)

sum = 0
for i in range(0,1000):
	sum += fdigit(i)

print (sum + 11)
