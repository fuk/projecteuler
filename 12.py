import itertools,math

def divisibleTriangle():
	triangleNumber = 0
	for i in itertools.count(1):
		triangleNumber += i
		if findDivisors(triangleNumber) > 500:
			return triangleNumber
			
def findDivisors(inputNumber):
	divisorsNumber = 0 
	endLimit = int(math.floor(math.sqrt(inputNumber)))
	for i in range(1,endLimit+1):
		if inputNumber % i == 0:
			divisorsNumber += 2
	if endLimit**2 == inputNumber:
		divisorsNumber -= 1
	return divisorsNumber

print(divisibleTriangle())