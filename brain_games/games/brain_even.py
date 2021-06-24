import random


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    number = random.randint(1, 100)
    return number, is_even(number)


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'
