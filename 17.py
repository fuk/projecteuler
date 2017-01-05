def numberCountLetters(inputNumber):
	totalLetters = 0
	if (inputNumber > 100):
		totalLetters += len(firstTen[(inputNumber/100)-1]+remainTens[-1]) + len('and') 
	if (inputNumber % 100 > 20):
		totalLetters +=  len(remainTens[((inputNumber/10)%10 - 1)])+ len(firstTen[((inputNumber%100)%10)-1])
	elif (inputNumber % 100 > 10):
		totalLetters +=  len(secondTen[((inputNumber%100)%10)-1])
	else:
		totalLetters += len(firstTen[inputNumber%100-1])
	return totalLetters


firstTen = ['one','two','three','four','five','six','seven','eight','nine','ten']
secondTen = ['eleven','twelve','thrirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
remainTens = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred']

def calculateSum():
	sumCounts = 0
	for i in range(1,1000):
		sumCounts += numberCountLetters(i)
	return sumCounts

print(calculateSum())