# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

factors = []
target = 600851475143
start = 2

# Check if Prime
def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

# Find first prime factor and add to list
def find_factor(n):
	for a in range(2, round(n / 2)):
		if is_prime(a):
			if n % a == 0:
				factors.append(a)
				if is_prime(n/a):
					factors.append(int(n/a))
				return n / a 

while is_prime(target) == False:
	target = find_factor(target)

print (max(factors))

	