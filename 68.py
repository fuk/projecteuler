def maxPath(triangle):
	triangleLen = len(triangle)-1
	for key, item in enumerate(triangle[:0:-1]):
		for subKey,value in enumerate(item[:-1]):
			if (item[subKey] >= item[subKey+1]):
				triangle[triangleLen-key-1][subKey] += item[subKey]
			else:
				triangle[triangleLen-key-1][subKey] += item[subKey+1]		
	return triangle[0][0]

def createTriangle(text):
	tempData = [x for x in text.split('\n')]
	return [map(int,x.split()) for x in tempData][1:-1]

# print(maxPath(createTriangle(WHATEVER YOU WANT)))
