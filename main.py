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
    ...


def train_until_mistake(words):
    ...


def add_words(words):
    ...


def show_all_words(words):
    ...


def save_words(words, filename):
    ...


def main():
    words = load_words('words.txt')
    print(f"Было загружено {len(words)} слов из файла words.txt")
    # while True:
    #     menu = '''Меню:
    #     1. Начать игру
    #     2. Добавить слова
    #     3. Тренировка до первой ошибки
    #     4. Вывод всех слов
    #     5. Выход
    #     '''
    #     print(menu)
    #     menu_choice = input('Пункт меню: ')


if __name__ == '__main__':
    main()