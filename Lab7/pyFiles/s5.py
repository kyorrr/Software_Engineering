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
