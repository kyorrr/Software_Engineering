import re
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        return words

def main():
    file_path = 's1.txt'
    words = count_words(file_path)

    word_count = len(words)
    print(f"Количество слов в тексте: {word_count}")

    word_freq = Counter(words)
    most_common_word, frequency = word_freq.most_common(1)[0]
    print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {frequency} раз)")

if __name__ == "__main__":
    main()