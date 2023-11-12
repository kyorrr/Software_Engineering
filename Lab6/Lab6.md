# Тема 6. Базовые коллекции: словари, кортежи.
Отчет по Теме #6 выполнил(а):
- Морозов Семен Игоревич
- ПИЭ-21-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Обработка данных пользователя в странной форме

```python
u_input = input("Введите последовательность чисел, разделенных пробелами: ")

numbers = u_input.split()

number_list = [int(num) for num in numbers]
number_tuple = tuple(number_list)

print("Список:", number_list)
print("Кортеж:", number_tuple)
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_6/Lab6/pic/1.png)

## Выводы

Программа распределяет введенные данные по списку и кортежу.

## Самостоятельная работа №2
### Неизменяемые кортежи Коли

```python
def remove_tuple(input_tuple, element_to_remove):
    if element_to_remove in input_tuple:
        index = input_tuple.index(element_to_remove)
        return input_tuple[:index] + input_tuple[index+1:]
    else:
        return input_tuple

tuple1 = (1, 2, 3)
result1 = remove_tuple(tuple1, 1)
print(result1)

tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
result2 = remove_tuple(tuple2, 3)
print(result2)

tuple3 = (2, 4, 6, 6, 4, 2)
result3 = remove_tuple(tuple3, 9)
print(result3)
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_6/Lab6/pic/2.png)

## Выводы

Программа удаляет первое появление элемента кортежа и возвращает уже без него.

## Самостоятельная работа №3
### Numpad

```python
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
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_6/Lab6/pic/3.png)

## Выводы

Программа выводит 3 самых частых числа)

## Самостоятельная работа №4
### Друг с офисом

```python
def find_employee_entry_exit(log, employee_id):
    if employee_id not in log:
        return ()

    start_index = log.index(employee_id)
    end_index = log[start_index + 1:].index(employee_id) + start_index + 1 if employee_id in log[start_index + 1:] else None

    if end_index is None:
        return log[start_index:]
    else:
        return log[start_index:end_index + 1]

log1 = (1, 2, 3)
employee_id1 = 8
result1 = find_employee_entry_exit(log1, employee_id1)
print(result1)

log2 = (1, 8, 3, 4, 8, 8, 9, 2)
employee_id2 = 8
result2 = find_employee_entry_exit(log2, employee_id2)
print(result2)

log3 = (1, 2, 8, 5, 1, 2, 9)
employee_id3 = 8
result3 = find_employee_entry_exit(log3, employee_id3)
print(result3)
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_6/Lab6/pic/4.png)

## Выводы

Ничего нового. Извините уже просто комментарий нет.

## Самостоятельная работа №5
### Мое задание

```python
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
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_6/Lab6/pic/5.png)

## Выводы

 Задача на нахождение наибольшего и наименьшего чисел в списке. 

## Общие выводы
Это самая сложная тема за все время. Пришлось посидеть и подумать, и даже погуглить, но я справился.
