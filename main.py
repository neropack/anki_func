import random
import sys
import os
import time
from typing import Dict, Tuple


STOP_WORD = 'СТОП'


def load_words(filename):
    words = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if ' - ' in line:
                    parts = line.split(' - ', 1)
                    if len(parts) == 2:
                        word, translation = parts
                        words[word.strip()] = translation.strip()
    except FileNotFoundError:
        print("Файл words.txt не найден.")
        sys.exit(1)
    return words
    


def print_statistics(score, total_time):
    ...


def ask_and_check(word, correct):
    ...


def start_game(words):
    if not words:
        print("Словарь пуст. Добавьте слова перед началом игры.")
        return
    print("Чтобы закончить, введите СТОП")
    score = 0
    total_time = 0.0
    while True:
        word = random.choice(list(words.keys()))
        start_time = time.time()
        translation = input(f"Ваше слово: {word}\nВаш перевод: ").strip()
        end_time = time.time()
        response_time = end_time - start_time
        total_time += response_time
        if translation.upper() == STOP_WORD.upper():
            break
        correct_translation = words[word]
        if translation == correct_translation:
            print(f"Верно! Время на ответ: {response_time:.2f} секунд")
            score += 1
        else:
            print(f"Неправильно, правильный ответ: {correct_translation} (Время на ответ: {response_time:.2f} секунд)")
    print("Спасибо за игру!")
    # print_statistics(score, total_time)


def train_until_mistake(words):
    ...


def add_words(words):
    print("Чтобы закончить, введите СТОП")
    while True:
        word = input("Введите слово: ").strip()
        if word.upper() == STOP_WORD.upper():
            break
        translation = input("Введите перевод: ").strip()
        if translation.upper() == STOP_WORD.upper():
            break
        words[word] = translation


def show_all_words(words):
    if not words:
        print("")
        return
    pairs = [f"{word} - {translation}" for word, translation in words.items()]
    output = "; ".join(pairs)
    print(output)


def save_words(words, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for word, translation in words.items():
            f.write(f"{word} - {translation}\n")
    print(f"Было сохранено {len(words)} слов в файл {filename}")


def main():
    filename = os.path.join(os.path.dirname(__file__), 'words.txt')
    words = load_words(filename)
    print(f"Было загружено {len(words)} слов из файла words.txt")
    while True:
        menu = '''Меню:
        1. Начать игру
        2. Добавить слова
        3. Тренировка до первой ошибки
        4. Вывод всех слов
        5. Выход
        '''
        print(menu)
        menu_choice = input('Пункт меню: ')

        if menu_choice == '1':
            start_game(words)
        elif menu_choice == '2':
            add_words(words)
        elif menu_choice == '3':
            train_until_mistake(words)
        elif menu_choice == '4':
            show_all_words(words)
        elif menu_choice == '5':
            save_words(words, 'words.txt')
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == '__main__':
    main()