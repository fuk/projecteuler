def diff(n):
	return 2 * sum([x*y for x in range (1,n) for y in range(x+1,n+1)])

print(diff(100))