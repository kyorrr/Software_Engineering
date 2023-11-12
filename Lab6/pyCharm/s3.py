def create_dict(input_string):
    digit_count = {}

    for digit in input_string:
        if digit.isdigit():
            digit = int(digit)
            digit_count[digit] = digit_count.get(digit, 0) + 1

    sorted_digit_count = dict(sorted(digit_count.items(), key=lambda item: item[1], reverse=True))
    top_3_most_common = dict(list(sorted_digit_count.items())[:3])

    return top_3_most_common


user_input = input("Введите строку с числами (не менее 15 символов): ")

if len(user_input) < 15:
    print("Длина строки должна быть больше 15 символов.")
else:
    result_dict = create_dict(user_input)
    sorted_result_dict = dict(sorted(result_dict.items()))
    print("3 самых частых числа:", sorted_result_dict)