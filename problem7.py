# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

primes = 0
stop_at = 10001
nth_prime = 0

# Check if Prime
def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

j = 2
while j > 0:
	if is_prime(j):
		primes += 1
		if primes == stop_at:
			nth_prime = j
			break
	j = j + 1

print (nth_prime)