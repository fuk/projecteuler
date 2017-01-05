def compute():
	return max(range(1, 1000000), key=collatz_chain_length)
	
collatz_cache = {1: 1}

def collatz_chain_length(x):
	if x not in collatz_cache:
		if x % 2 == 0:
			y = x // 2
		else:
			y = x * 3 + 1
		collatz_cache[x] = collatz_chain_length(y) + 1
	return collatz_cache[x]


print(compute())