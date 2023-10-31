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