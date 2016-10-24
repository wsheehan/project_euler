# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# 500 because others sides together must be longer than c
triplets = []

for a in range(1,500):
	for b in range(1,500):
		c2 = a**2 + b**2
		if c2**0.5 % 1 == 0:
			triplets.append([a,b,int(c2**0.5)])

def find_triplet(list):
	for i in triplets:
		if sum(i) == 1000:
			return i

triplet = find_triplet(triplets)

print (triplet[0]*triplet[1]*triplet[2])

