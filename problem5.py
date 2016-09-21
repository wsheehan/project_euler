# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

maxInt = 20
x = 0
i = maxInt * (maxInt - 1)

def is_divisible_by_all(n):
	for j in reversed(range(2, maxInt + 1)):
		if n % j != 0:
			return False
	x = n		
	return True

while is_divisible_by_all(i) == False:
	i += maxInt

print (i)
