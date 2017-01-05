from fractions import gcd

print(reduce(lambda a, b: a * b / gcd(a, b), range(1, 21)))