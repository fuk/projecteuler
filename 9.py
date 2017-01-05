from operator import mul

def isPythagorean(x,y,z):
	return (x**2 + y**2 == z**2)
def findPythagorean():
	for x in range(1,1000):
		for y in range(x,1000-x):
			z = 1000 - x - y
			if z < y:
				break
			if isPythagorean(x,y,z):
				return reduce(mul,[x,y,z])

print(findPythagorean())