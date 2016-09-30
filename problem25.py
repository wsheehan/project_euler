# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def get_next_fibonacci(x,y):
	return [y,x+y]

i = [1,1]
upper = 10**999
#upper = 89
j = 2
while j > 0:
	i = get_next_fibonacci(i[0],i[1])
	if i[1] % upper != i[1]:
		break
	else:
		j += 1

print (j+1)

