#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import random
import sys
import argparse

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='?', default='dictionary.txt')  # словарь по умолчанию
    return parser


def enter_rus_word():
    entered_word = input('Input translate word: ' + '\x1b[01;32m')
    print('\x1b[0m')
    # if entered_word == '':
    #     entered_word = 'ничего_не_введено'
    return entered_word


def main():

    # Очистить консоль
    clear_сonsole()

    # Обработать параметр командной строки - имя файла-словаря
    my_parser = create_parser()    # Экземпляр парсера
    namespace = my_parser.parse_args(sys.argv[1:])
    # print(namespace)
    dict_file_name = namespace.name     # имя файла-словаря

    # Открыть файл, считать его и закрыть
    file_wrapper = open(dict_file_name, encoding='UTF-8')
    lines = file_wrapper.readlines()
    file_wrapper.close()

    # Получить словарь из файла
    dict_eng_rus = get_dict_eng_rus(lines)
    # print(dict_eng_rus)

    # Получить случайное английское слово
    random_word = get_random_word(lines)
    print('English word: ' + random_word)

    # Ввод перевода (русского слова
    entered_word = enter_rus_word()

    # Выход из программы
    if entered_word == 'q' or entered_word == 'Q' or \
       entered_word == 'й' or entered_word == 'Й':
        clear_сonsole()
        print('Bye-bye!')
        sys.exit()

    # Получить перевод из файла
    translated_words = get_translated_words(random_word, dict_eng_rus)

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

    result = ''

    for word in translated_words:
        if entered_word.lower() != word.lower():
            result = bold_red_color + 'Ошибка!' + default_attributes + ' => '
            for string in translated_words:
                result += bold_blue_color + string
                result += '  '
        else:
            result = bold_test_color + 'Верно.' + default_attributes
            break
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

        # Удалить запятую
        rus_words = []
        for word in one_line.split()[1:]:
            word = word.replace(',', '')
            # print(word)
            rus_words.append(word)

        # Сформировать словарь
        dictionary_eng_rus.update({one_line.split()[0]: rus_words})

    return dictionary_eng_rus


def get_translated_words(random_word, dict_eng_rus):
    # print(dict_eng_rus)
    # print('Рандом ворд: ' + random_word)
    transl_words = dict_eng_rus[random_word]
    # print(transl_words)
    return transl_words


def get_random_word(lines):
    # Выбрать первый столбец - английские слова
    english_word = []
    for one_line in lines:
        english_word.append(one_line.split()[0])
    # print(english_word)

    # Венуть случайное слово
    random.seed(version=2)          # Инициализация временем
    return random.choice(english_word)


if __name__ == "__main__":
    my_counter = Counter()
    while True:
        main()
