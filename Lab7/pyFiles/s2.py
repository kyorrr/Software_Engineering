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
