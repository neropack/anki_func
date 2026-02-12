import random
import sys
import os
import time
from typing import Dict, Tuple


STOP_WORD = 'СТОП'


def load_words(filename: str) -> Dict[str, str]:
    """
    Загружает пары «слово, перевод» из текстового файла и формирует словарь.
    """
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


def print_statistics(score: int, total_time: float) -> None:
    """
    Выводит итоговую статистику игры: счёт, общее и среднее время на ответ.
    """
    if score == 0:
        average = "—"
    else:
        average = f"{total_time / score:.2f}"
    print(f"Ваш итоговый счёт: {score}")
    print(
        f"Время игры: {total_time:.2f} секунд (среднее время: {average} сек.)")


def ask_and_check(word: str, correct: str) -> Tuple[bool, bool, float]:
    """
    Запрашивает у пользователя перевод слова, проверяет его и возвращает
    результаты.
    """
    print(f"Ваше слово: {word}")
    start_time = time.time()
    translation = input("Ваш перевод: ").strip()
    end_time = time.time()
    response_time = end_time - start_time
    if translation.upper() == STOP_WORD.upper():
        return True, False, 0.0
    is_correct = translation.lower() == correct.lower()
    return False, is_correct, response_time


def start_game(words: Dict[str, str]) -> None:
    """
    Запускает обычный игровой режим тренировки слов.
    """
    if not words:
        print("Словарь пуст. Добавьте слова перед началом игры.")
        return
    print("Чтобы закончить, введите СТОП")
    score = 0
    total_time = 0.0
    while True:
        word = random.choice(list(words.keys()))
        exit_flag, is_correct, response_time = ask_and_check(word, words[word])
        total_time += response_time
        if exit_flag:
            break
        if is_correct:
            print(f"Верно! Время на ответ: {response_time:.2f} секунд")
            score += 1
        else:
            print(
                f"Неправильно, правильный ответ: {words[word]} (Время на ответ: {response_time:.2f} секунд)")
    print("Спасибо за игру!")
    print_statistics(score, total_time)


def train_until_mistake(words: Dict[str, str]) -> None:
    """
    Запускает режим тренировки «до первой ошибки».
    """
    if not words:
        print("Словарь пуст. Добавьте слова перед началом игры.")
        return
    print("Режим: игра до первой ошибки! Чтобы выйти вручную, введите СТОП")
    word_list = list(words.keys())
    score = 0
    total_time = 0.0
    while True:
        word = random.choice(word_list)
        exit_flag, is_correct, response_time = ask_and_check(word, words[word])
        total_time += response_time
        if exit_flag:
            print("Выход из режима по запросу пользователя.")
            break
        if is_correct:
            score += 1
            print(
                f"Верно! Всего очков: {score} (ответ за {response_time:.2f} секунд)")
        else:
            print(f"Ошибка! Неверно. Правильный ответ: {words[word]}")
            break
    print_statistics(score, total_time)


def add_words(words: Dict[str, str]) -> None:
    """
    Добавляет новые пары слово-перевод в словарь в интерактивном режиме.
    """
    print("Чтобы закончить, введите СТОП")
    while True:
        word = input("Введите слово: ").strip()
        if word.upper() == STOP_WORD.upper():
            break
        translation = input("Введите перевод: ").strip()
        if translation.upper() == STOP_WORD.upper():
            break
        words[word] = translation


def show_all_words(words: Dict[str, str]) -> None:
    """
    Выводит все пары слово-перевод из словаря в одну строку.
    """
    if not words:
        print("")
        return
    pairs = [f"{word} - {translation}" for word, translation in words.items()]
    output = "; ".join(pairs)
    print(output)


def save_words(words: Dict[str, str], filename: str) -> None:
    """
    Сохраняет словарь в файл и выводит сообщение о сохранении.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for word, translation in words.items():
            f.write(f"{word} - {translation}\n")
    print(f"Было сохранено {len(words)} слов в файл {filename}")


def main() -> None:
    """
    Основной цикл программы: загружает словарь, отображает меню и обрабатывает
    выбор пользователя.
    """
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
