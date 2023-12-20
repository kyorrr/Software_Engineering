def add_two_and_number():
    try:
        user_input = input("Введите число: ")
        result = 2 + float(user_input)
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    # Тест 1: ввод корректного числа
    add_two_and_number(10)

    # Тест 2: ввод строки вместо числа
    add_two_and_number("fjskf")

    # Тест 3: ввод другого неподходящего типа данных
    add_two_and_number("-2")
