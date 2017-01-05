import itertools

def cubicPermutation():
	dictDigits = {}

	for i in itertools.count():
	    cube = i*i*i
	    digits = ''.join(sorted(str(cube)))

	    if digits in dictDigits:
	        dictDigits[digits] += [cube]
	        if len(dictDigits[digits]) == 5:
	            break
	    else:
	        dictDigits[digits] = [cube]
	return min(dictDigits[digits])

print(cubicPermutation())