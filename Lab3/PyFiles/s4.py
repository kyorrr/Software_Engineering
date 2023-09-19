sent = str(input("Введите ваше предложение на английском языке: "))

print(f'Ваше предложение: {sent}')

length = len(sent)
print("Длина вашего предложения:", length)

lowerCase = sent.lower()
print("Ваше предложение в нижнем регистре", lowerCase)

values = 'aeiouAEIOU'
counter = 0

for vowel in sent:
    if vowel in values:
        counter += 1
print("Количество гласных a, e, i, o, u(считая верхний и нижний регистр): ", counter)

sent_modified = lowerCase.replace("ugly", "beauty")
print("Измененное предложение: ", sent_modified)

if sent.startswith("The"):
    print("Предложение начинается с 'The'")
elif sent.endswith("end."):
    print("Предложение заканчивается на 'end.'")
else:
    print("Предложение не начинается с 'The' и не заканчивается на 'end'")