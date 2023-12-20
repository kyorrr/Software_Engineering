def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content:
                raise Exception("Файл пустой")
            else:
                print("Информация из файла:")
                print(content)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден")
    except Exception as e:
        print(f"Исключение: {e}")

if __name__ == '__main__':
    # Пример использования для пустого файла
    print("Для пустого файла:")
    read_file('empty_file.txt')

    print("\n" + "="*30 + "\n")

    # Пример использования для файла с информацией
    print("Для файла с информацией:")
    read_file('non_empty_file.txt')

