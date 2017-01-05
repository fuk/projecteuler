def even_fib(limit):
    a, b = 1, 2
    while a < limit:
        if not a % 2:         
            yield a
        a, b = b, a + b

print sum(even_fib(4000000))