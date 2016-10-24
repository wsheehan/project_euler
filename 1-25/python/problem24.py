# A permutation is an ordered arrangement of objects. For example, 
# 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

n = 2

lexn = 0
lex = []
# for i in range(0,n+1):
# 	l = [i]
# 	for j in range(0,n+1):
# 		if j not in l:
# 			l = [i,j]
# 			for k in range(0,n+1):
# 				if k not in l:
# 					lex.append([i,j,k])
			

def get_lex(n,m,l):
	for i in range(0,n+1):
		if i not in l:
			if n == m:
				lex.append(l+[i])
				return True
			else:
				return l + [i]
 
j = 0
l = []
while get_lex(n,j,l) != True:
	for i in range(0,n+1):
		l = get_lex(n,j,l)
	j += 1

print (lex)

