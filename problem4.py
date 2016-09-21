# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

order = 3
x = 100**order
palindrome = 0

def is_palindrome(n):
	return str(n) == str(n)[::-1]

def is_3digit_product(n):
	i = 10**order - 1
	while i > 10**(order - 1):
		if n % i == 0 and n / i >= 10**(order-1) and n / i < 10**order:
			return True
		i -= 1
	return False

while x > 10**(order-1):
	if is_palindrome(x) and is_3digit_product(x):
		palindrome = x
		break
	x -= 1

print (palindrome)
