import random


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def make_question():
    first_number = random.randint(1, 30)
    second_number = random.randint(1, 30)
    question = "{} {}".format(first_number, second_number)
    correct_answer = str(gcd(first_number, second_number))
    return question, correct_answer


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
