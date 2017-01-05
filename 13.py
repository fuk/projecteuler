def sum50digits(text):
	return str(sum([int(x) for x in text.split('\n')]))[:10]
