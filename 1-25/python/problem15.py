# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

def factorial(n):
	p = n
	while n > 1:
		p *= (n-1)
		n -= 1
	return p

def combinations(n):
	return int(factorial(2*n)/(factorial(n)*factorial(n)))

print (combinations(20))
