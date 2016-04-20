#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import random
import sys
import argparse

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


def create_parser(default_dictionary):
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='?', default=default_dictionary)
    return parser


def enter_rus_word():
    entered_word = input('Input translate word: ' + '\x1b[01;32m')
    print('\x1b[0m')
    return entered_word


def main():

    # Очистить консоль
    clear_сonsole()

    # Обработать параметр командной строки - имя файла-словаря
    default_dictionary = 'dictionary.txt'               # файл-словарь по умолчанию
    my_parser = create_parser(default_dictionary)       # Экземпляр парсера
    namespace = my_parser.parse_args(sys.argv[1:])
    dict_file_name = namespace.name                     # имя файла-словаря

    # Открыть файл, считать его и закрыть
    file_wrapper = open(dict_file_name, encoding='UTF-8')
    lines = file_wrapper.readlines()                    # список строк файла
    file_wrapper.close()

    # Получить слова из файла и поместить в словарь Питоновский
    dict_eng_rus = get_dict_eng_rus(lines)
    # Список иностранных слов из ключей словаря
    my_keys = list(dict_eng_rus.keys())
    # Получить случайное английское слово
    random_word = get_random_line(my_keys)
    print('English word: ' + random_word)

    # Получить перевод из словаря по ключу
    translated_words = dict_eng_rus[random_word]

    # Ввод перевода (русского слова)
    entered_word = enter_rus_word()

    # Выход из программы
    if entered_word == 'q' or entered_word == 'Q' or \
       entered_word == 'й' or entered_word == 'Й':
        clear_сonsole()
        print('Bye-bye!')
        sys.exit()

    # Проверить правильность перевода
    conclusion = correctness_translate(entered_word, translated_words)

    # Вывод результата
    print(random_word + ' => ' + entered_word)
    print(conclusion)
    print()
    print('Gud: {0},  Bad: {1}, Gud percent: {2:3.0f}%.'
          .format(str(my_counter.get_count_gud()),
                  str(my_counter.get_count_bad()),
                  my_counter.get_percent_gud()))
    input('Press Enter to continue.')


class Counter:
    count_gud = 0
    count_bad = 0

    def gud_count_increment(self):
        self.count_gud += 1

    def bad_count_increment(self):
        self.count_bad += 1

    def get_count_gud(self):
        return self.count_gud

    def get_count_bad(self):
        return self.count_bad

    def get_percent_gud(self):
        percent_gud = 100 * self.count_gud / (self.count_gud + self.count_bad)
        return percent_gud


def correctness_translate(entered_word, translated_words):

    # Цвета и атрибуты шрифта для консоли
    default_attributes = '\x1b[0m'
    bold_red_color = '\x1b[01;31m'
    bold_blue_color = '\x1b[01;34m'
    bold_test_color = '\x1b[01;32m'

    if entered_word.lower() not in translated_words.lower() or entered_word == '':
        result = bold_red_color + 'Ошибка!' + default_attributes + ' => '
        result += bold_blue_color + translated_words
    else:
        result = bold_test_color + 'Верно.' + default_attributes
    result += default_attributes

    if result.find('Верно.') is not -1:
        my_counter.gud_count_increment()
    else:
        my_counter.bad_count_increment()

    return result


def clear_сonsole():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def get_dict_eng_rus(lines):
    dictionary_eng_rus = {}
    for one_line in lines:
        foreign_word = one_line.split('=')[0].strip()
        rus_words = one_line.split('=')[1].strip()
        dictionary_eng_rus.update({foreign_word: rus_words})
    return dictionary_eng_rus


def get_random_line(word):
    # Вернуть случайное слово
    random.seed(version=2)                  # Инициализация временем
    return random.choice(word)


if __name__ == "__main__":
    my_counter = Counter()
    while True:
        main()
