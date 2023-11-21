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
