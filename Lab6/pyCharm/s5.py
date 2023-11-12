def find_min_max(numbers):
    if not numbers:
        return None, None

    min_number = min(numbers)
    max_number = max(numbers)

    return min_number, max_number


# Примеры использования функции
numbers1 = [5, 2, 9, 1, 8, 3]
result1 = find_min_max(numbers1)
print(result1)

numbers2 = [10, 10, 10, 10]
result2 = find_min_max(numbers2)
print(result2)

numbers3 = []
result3 = find_min_max(numbers3)
print(result3)
