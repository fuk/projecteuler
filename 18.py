def spiral(edge):
	finalSum = 0
	pointNum = 1
	for x in range(2,edge,2):
		for y in range(4):
			pointNum += x
			finalSum += pointNum
	return (finalSum+1)

print(spiral(1001))




# def g(n):
#     s = (n-1) // 2
#     return (16*s*s*s + 30*s*s + 26*s + 3) // 3
