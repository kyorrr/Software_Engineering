user_input = input("Введите последовательность чисел, разделенных пробелами: ")

numbers = user_input.split()

number_list = [int(num) for num in numbers]
number_tuple = tuple(number_list)

print("Список:", number_list)
print("Кортеж:", number_tuple)