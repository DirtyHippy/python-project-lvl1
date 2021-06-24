import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
