# Тема 7. Работа с файлами(ввод, вывод).
## Сразу извиняюсь, что сдаю работы поздно и не вовремя. Очень много всего навалилось: как все решу(2 дня примерно) сразу сяду делать ваши задания.
Отчет по Теме #7 выполнил(а):
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
### Статья

```python
import re
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        return words

def main():
    file_path = 's1.txt'
    words = count_words(file_path)

    word_count = len(words)
    print(f"Количество слов в тексте: {word_count}")

    word_freq = Counter(words)
    most_common_word, frequency = word_freq.most_common(1)[0]
    print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {frequency} раз)")

if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/Lab7/pic/1.png)

## Выводы

Программа открывает текстовый файл с каким-нибудь текстом, считает там слова и находит самое популярное слово в тексте.

## Самостоятельная работа №2
### Контроль расходов

```python
import csv
import os

def create_expense_file(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Дата", "Категория", "Сумма", "Примечание"])

def add_expense(file_name, date, category, amount, note):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

def display_expenses(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    file_name = "s2.csv"

    if not os.path.isfile(file_name):
        create_expense_file(file_name)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить расход")
        print("2. Просмотреть все расходы")
        print("3. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            date = input("Введите дату (формат: ГГГГ-ММ-ДД): ")
            category = input("Введите категорию расхода: ")
            amount = input("Введите сумму расхода: ")
            note = input("Введите примечание: ")

            add_expense(file_name, date, category, amount, note)
            print("Расход добавлен успешно!")

        elif choice == "2":
            print("\nВсе расходы:")
            display_expenses(file_name)

        elif choice == "3":
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие снова.")

if __name__ == "__main__":
    main()

```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/Lab7/pic/2.png)
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/Lab7/pic/2.1.png)

## Выводы

Программа создает текстовый файл и записывает в него расходы на определенное число с примечанием. Также файл редактируется, и можно было бы даже добавить функцию удаления расходов. Всей программой управляем из консоли.

## Самостоятельная работа №3
### Счет букв, слов и строк в английском тексте

```python
def calculate_statistics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            latin_letters_count = sum(c.isalpha() and c.isascii() for c in content)

            words_count = len(content.split())

            lines_count = content.count('\n') + 1

            print(f"Количество букв латинского алфавита: {latin_letters_count}")
            print(f"Число слов: {words_count}")
            print(f"Число строк: {lines_count}")

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = 's3.txt'

calculate_statistics(file_path)
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/Lab7/pic/3.png)

## Выводы

Программа берет данные из текстового файла, а именно текс написанный на латиннице, и считает сколько всего букв, слов и строк в данном тексте.

## Самостоятельная работа №4
### Цензура

```python
import re

def censor_sentence(sentence, banned_words):
    for word in banned_words:
        sentence = sentence.replace(word, '*' * len(word))
        sentence = sentence.replace(word.capitalize(), '*' * len(word))
        sentence = sentence.replace(word.upper(), '*' * len(word))
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        sentence = pattern.sub('*' * len(word), sentence)
    return sentence

def main():
    with open('s4.txt', 'r') as file:
        banned_words = file.read().split()

    sentence = input("Введите предложение: ")

    censored_sentence = censor_sentence(sentence, banned_words)

    print("Ожидаемый результат:", censored_sentence)

if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/Lab7/pic/4.png)

## Выводы

Одна из самых сложных самостоятельных в последнее время. Не получалось написать нормально функцию, но в общем и целом справился. Программа берет текст из консоли, сверяет каждое цензурное слово, которое можно добавить в текстовый файл и выводит измененный текст.

## Самостоятельная работа №5
### Мое задание
### Допустим, у вас есть текстовый файл, в котором записаны оценки студентов по разным предметам. Каждая строка файла представляет собой запись вида "Имя_студента Предмет Оценка".

### Задача: напишите программу на языке программирования по вашему выбору, которая будет анализировать этот файл и выводить средние оценки для каждого студента.

### Пример файла (students.txt):

Иван Математика 4
Иван Математика 5
Иван Физика 3
Мария Математика 5
Мария Физика 4
Мария Английский 5
Петр Математика 3
Петр Физика 5
Петр Английский 4

### Программа должна считывать файл, а затем вычислять средние оценки для каждого студента и выводить результаты. Например:

Средняя оценка Ивана: 4.0
Средняя оценка Марии: 4.67
Средняя оценка Петра: 4.0

```python
# Открываем файл для чтения
with open('s5.txt', 'r') as file:
    # Инициализируем словарь для хранения суммы оценок и количества предметов для каждого студента
    student_scores = {}

    # Читаем каждую строку файла
    for line in file:
        # Разбиваем строку на части по пробелу
        parts = line.split()

        # Извлекаем имя студента, предмет и оценку
        student_name = parts[0]
        subject = parts[1]
        score = float(parts[2])  # Преобразуем оценку в число

        # Проверяем, есть ли уже запись для студента в словаре
        if student_name in student_scores:
            # Если запись существует, обновляем сумму оценок и количество предметов
            student_scores[student_name][0] += score
            student_scores[student_name][1] += 1
        else:
            # Если записи нет, создаем новую запись для студента
            student_scores[student_name] = [score, 1]

# Выводим средние оценки для каждого студента
for student_name, scores in student_scores.items():
    average_score = scores[0] / scores[1]
    print(f"Средняя оценка {student_name}: {average_score:.2f}")
```
### Результат.
![Меню](https://github.com/kyorrr/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/Lab7/pic/5.png)

## Выводы

 Собственная задача сразу идет с входной информацией и данными. В общем берется из текстового файла данные об учениках и их оценки и в конце концов считается средний балл каждого ученика. 

## Общие выводы
Я заметил, что каждый раз надо думать все больше и больше. Это хорошо) В целом сама тема не особо сложная, но посидеть и подумать было надо. Выучил много лексикона и библиотек с их функционалом.
