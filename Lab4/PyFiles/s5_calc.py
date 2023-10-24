from s5 import geron

def get_input(sides):
    while True:
        try:
            value = float(input(sides))
            return value
        except ValueError:
            print("Пожалуйста, введите числовое значение.")

def main():
    print("Введите длины сторон треугольника:")
    a = get_input("Длина стороны A: ")
    b = get_input("Длина стороны B: ")
    c = get_input("Длина стороны C: ")

    if a + b > c and a + c > b and b + c > a:
        calc = geron(a, b, c)
        print(f"Площадь треугольника, рассчитанная по формуле Герона: {calc:.2f}")
    else:
        print("Треугольник с такими сторонами не может существует.")


if __name__ == '__main__':
    main()