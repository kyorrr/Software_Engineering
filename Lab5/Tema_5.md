# Тема 5. Базовые коллекции: множества, списки.
Отчет по Теме #5 выполнил(а):
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
### Учет в ресторане

```python
receipts = [8734, 2345, 8201, 6621, 9999, 1234, 5678,
         8201, 8888, 4321, 3365, 1478, 9865, 5555,
         7777, 9998, 1111, 2222, 3333, 4444, 5556,
         6666, 5410, 7778, 8889, 4445, 1439, 9604,
         8201, 3365, 7502, 3016, 4928, 5837, 8201,
         2643, 5017, 9682, 8530, 3250, 7193, 9051,
         4506, 1987, 3365, 5410, 7168, 7777, 9865,
         5678, 8201, 4445, 3016, 4506, 4506]

total_receipts = len(receipts)

unique_receipts = len(set(receipts))

max_receipts = max(set(receipts), key=receipts.count)

print("Выдано чеков: ", total_receipts)
print("Уникальные работники: ", unique_receipts)
print("Самый работящий: ", max_receipts)
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_5/Lab5/pic/1.png)

## Выводы

Через len программа считает общее кол-во чеков, затем считает уол-во уникальных номеров и потом ищет, который из них встречается чаще всего.

## Самостоятельная работа №2
### Бег студентов.

```python
runners = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1,
           38.9, 21.6, 26.4, 17.1, 30.2, 35.7,
           16.9, 27.8, 24.5, 16.3, 18.7, 31.9,
           12.9, 37.4]

the_best = sorted(runners)[:3]
the_worst = sorted(runners)[-3:]
ten_plus = sorted([result for result in runners if result >= 10])

print("3 Лучших: ", the_best)
print("3 Худших: ", the_worst)
print("Результаты больше 10: ", ten_plus)

```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_5/Lab5/pic/2.png)

## Выводы

Тот же алгоритм. Программа получает все данные, дальше из них выводит 3 лучших, 3 худших и все, что выше 10. В последнем результаты выводятся в порядке возрастания.

## Самостоятельная работа №3
### Это Мамалыга, опять воспоминания...

```python
import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def area(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

one_max = max(one)
one_min = min(one)
two_max = max(two)
two_min = min(two)
three_max = max(three)
three_min = min(three)

max_list = [one_max, two_max, three_max]
min_list = [one_min, two_min, three_min]

max_triangle = area(*max_list)
min_triangle = area(*min_list)

print("Макс. треугольник: ", round(max_triangle))
print("Мин. треугольник: ", round(min_triangle))
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_5/Lab5/pic/3.png)

## Выводы

Тут в целом все понятно, монотонный код. Самое главное это воспоминания с прошлых курсов...

## Самостоятельная работа №4
### Боря...

```python
def format_grades(grades):
    format_grades = [4 if grade == 3 else grade for grade in grades if grade != 2]
    return format_grades

grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

format_grades1 = format_grades(grades1)
format_grades2 = format_grades(grades2)
format_grades3 = format_grades(grades3)

print(format_grades1)
print(format_grades2)
print(format_grades3)
print("К сожалению Боре это не поможет :(")
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_5/Lab5/pic/4.png)

## Выводы

В задании надо было проверить работу программы отдельно на каждом списке, то и задаются в программу они отдельно. Сначала прописывается функция, дальше выводится то, что эта функция сделала со списками. Ну и подпись, что Боре это не поможет, это главное!!!!

## Самостоятельная работа №5
### Опять что-то непонятное.

```python
def transform_to_sets(input_list):
    result_set = set()
    num_count = {}

    for num in input_list:
        if num not in num_count:
            num_count[num] = 1
            result_set.add(num)
        else:
            num_count[num] += 1
            result_set.add(str(num) * num_count[num])

    return result_set


list1 = [1, 1, 3, 3, 1]
list2 = [5, 5, 5, 5, 5, 5, 5]
list3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

res1 = transform_to_sets(list1)
res2 = transform_to_sets(list2)
res3 = transform_to_sets(list3)

print(res1)
print(res2)
print(res3)
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_5/Lab5/pic/5.png)

## Выводы

Не сразу понял, что именно надо сделать. Потом пришло осознание и у меня почти сразу получилось решить задачу. Как всегда, в начале прописываем функцию,
затем прописываем в программе 3 списка, из которых она берет числа и прогоняет их по условиям той самой функции.

## Общие выводы:

Вроде изи, а вроде где-то и думать надо. Все равно Борьку жалко. А так синтаксиса ОЧЕЕЕЕЕНЬ много, у меня скоро голова лопнет..
