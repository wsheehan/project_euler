# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Check if Prime
def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

prime_sum = 0
i = 2
while i < 2000000:
	if is_prime(i):
		prime_sum += i
	i += 1

print (prime_sum)