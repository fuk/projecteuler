from operator import mul

def factorial(x):
	return reduce(mul,[i for i in range(1,x+1)])

print(sum([int(i) for i in str(factorial(100))]))