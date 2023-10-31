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
