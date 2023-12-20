class CustomError(Exception):
    def __init__(self, message="Произошла ошибка"):
        self.message = message
        super().__init__(self.message)

def process_user_data(name, age):
    try:
        if not name or not age:
            raise CustomError("Имя и возраст должны быть заполнены")

        if not isinstance(age, int) or age < 0:
            raise CustomError("Некорректный формат возраста")

        print(f"Данные пользователя: Имя - {name}, Возраст - {age} лет")
    except CustomError as e:
        print(f"Ошибка при обработке данных пользователя: {e}")

def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content:
                raise CustomError("Файл пустой")
            else:
                print(f"Содержимое файла: {content}")
    except CustomError as e:
        print(f"Ошибка при чтении файла: {e}")

if __name__ == '__main__':
    # Тест 1: Правильные данные пользователя
    process_user_data("John Doe", 30)

    # Тест 2: Некорректный возраст (вызовет исключение)
    process_user_data("Alice", -25)

    # Тест 3: Пустое имя пользователя (вызовет исключение)
    process_user_data("", 22)

    # Тест 4: Чтение содержимого файла
    read_file_content("example_file.txt")

    # Тест 5: Чтение из пустого файла (вызовет исключение)
    read_file_content("empty_file.txt")
