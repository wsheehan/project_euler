# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

n = 2**1000

s = 0
for ch in str(n):
	s += int(ch)

print (s)