import re

def censor_sentence(sentence, banned_words):
    for word in banned_words:
        sentence = sentence.replace(word, '*' * len(word))
        sentence = sentence.replace(word.capitalize(), '*' * len(word))
        sentence = sentence.replace(word.upper(), '*' * len(word))
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        sentence = pattern.sub('*' * len(word), sentence)
    return sentence

def main():
    with open('s4.txt', 'r') as file:
        banned_words = file.read().split()

    sentence = input("Введите предложение: ")

    censored_sentence = censor_sentence(sentence, banned_words)

    print("Ожидаемый результат:", censored_sentence)

if __name__ == "__main__":
    main()
