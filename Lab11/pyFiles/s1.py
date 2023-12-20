def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci_sequence = list(fib(10))
print(fibonacci_sequence)

fib_200 = next(fib(200))
print(fib_200)