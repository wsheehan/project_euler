# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import timeit

def sum_proper_divisors(n):
	l = []
	for i in range(1,int(n**0.5)+1):
		if n % i == 0:
			l.append(i)
			if i**2 != n and i != 1:
				l.append(int(n/i))
	return sum(l)

def is_abundant(n):
	if sum_proper_divisors(n) > n:
		return True
	else:
		return False

start_abundants = timeit.default_timer()

abundants = []
for i in range(0,28123+1):
	if is_abundant(i):
		abundants.append(i)

print("Time for abundants:", timeit.default_timer() - start_abundants)

start_abundants_sums = timeit.default_timer()

abundants_sums = []
print (len(abundants))
for i in abundants:
	for j in abundants:
		abundants_sums.append(i+j)

print("Time for abundant sum:", timeit.default_timer() - start_abundants_sums)

abundants_sums = list(set(abundants_sums))

start_no_sum = timeit.default_timer()

no_sum_total = 0
for i in range(1,28123+1):
	if i not in abundants_sums:
		no_sum_total += i

print("Time for no abundant sum:", timeit.default_timer() - start_no_sum)

print (no_sum_total)
