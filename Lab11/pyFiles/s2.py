def fib(n):
    a, b = 1, 1
    with open("fibonachi.txt", "w") as file:
        for _ in range(n):
            file.write(f"{a}\n")
            yield a
            a, b = b, a + b

fibonacci_sequence = list(fib(10))
print(fibonacci_sequence)

fib_200 = next(fib(200))
print(fib_200)