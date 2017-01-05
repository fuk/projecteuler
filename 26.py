from decimal import * 

def calcFloat(n):
	return str(Decimal(1)/Decimal(n))[2:]

def reciprocal_cycle_len(n):
	seen = {}
	x = 1
	i = 0
	while x not in seen:
		seen[x] = i
		x = x * 10 % n
		i += 1
	return i - seen[x]

print(reciprocal_cycle_len(7))