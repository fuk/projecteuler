from itertools import permutations, islice

print(''.join(next(islice(permutations('0123456789'), 1000000-1, None))))

