import random


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer


def is_even(number):
    return number % 2 == 0
