def avg():
    num = []

    print("Введите число или чтобы завершить ппрограмму нажмите 'Enter'")

    while True:
        u_inp = input("Введите число: ")

        if not u_inp.strip():
            break

        try:
            number = float(u_inp)
            num.append(number)
        except ValueError:
            print("Неверный формат числа.")

    if len(num) == 0:
        print("Не было введено ни одного числа.")
    else:
        total = sum(num)
        average = total/len(num)
        print(f'Среднее арифметическое чисел равна: {average}')

if __name__ == "__main__":
    avg()