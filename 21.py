def findDivisors():
	divisorsSum = [0] * 10000
	for x in range(1,10000):
		for y in range(2*x,10000,x):
			divisorsSum[y] += x

	amicablePairs = 0
	for x in range(1,10000):
		tempVar = divisorsSum[x]
		if (tempVar != x) and (tempVar < 10000) and (divisorsSum[tempVar] == x):
			amicablePairs += 1
	return amicablePairs

print(findDivisors())
