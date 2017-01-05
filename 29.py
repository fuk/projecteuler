def distinct(a,b):
	return [x**y for x in range(2, a+1 ) for y in range(2, b+1 )]

def sort(a):
	return sorted(list(set(a)))

print(len(sort(distinct(100,100))))

