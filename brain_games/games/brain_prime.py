import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer


def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number and number % divisor != 0:
        divisor += 1
    return divisor * divisor > number
