# from pprint import pprint

from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_characters = 'il1Lo0O'

chars = ''


def generate_password(password_length, chars_all):
    result = ''
    for _ in range(int(password_length)):
        result += choice(chars_all)
    return result


start_stop = 'y'
while start_stop == 'y':
    counter_user = input('Сколько паролей необходимо сгененрировать?')
    password_length_user = input('Длина пароля?')
    presence_digits = input('Пароль должен содержать цифры 0123456789?(y/n)')
    capital_letters = input('Включать ли заглавные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(y/n)')
    not_capital_letters = input('Включать ли строчные буквы bcdefghijklmnopqrstuvwxyz?(y/n)')
    symbols = input('Включать ли символы !#$%&*+-=?@^_?(y/n)')

    ambiguous_characters_user = input('Исключать ли неоднозначные символы il1Lo0O?(y/n)')

    if presence_digits == 'y':
        chars = chars + digits
    if capital_letters == 'y':
        chars = chars + lowercase_letters
    if not_capital_letters == 'y':
        chars = chars + uppercase_letters
    if symbols == 'y':
        chars = chars + punctuation
    if ambiguous_characters_user == 'y':
        for i in ambiguous_characters:
            chars.replace(i, '')

    if presence_digits == 'y' or capital_letters == 'y' or not_capital_letters == 'y' or symbols == 'y':
        for _ in range(int(counter_user)):
            print(generate_password(password_length_user, chars))
    else:
        print('Вы исключили все возможные данные для создания пароля.')

    print('', 'Запустить заново генератор паролей?', sep='\n')
    start_stop = input()
