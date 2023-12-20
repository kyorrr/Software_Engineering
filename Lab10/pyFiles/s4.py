import time

class TimingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {self.func.__name__}: {execution_time} секунд")
        return result

@TimingDecorator
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@TimingDecorator
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

if __name__ == '__main__':
    print(factorial(5))

    print(generate_squares(5))
