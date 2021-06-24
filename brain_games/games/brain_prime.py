import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    number = random.randint(1, 100)
    return number, is_prime(number)


def is_prime(n):
    if n < 2:
        return 'no'
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return 'yes' if d * d > n else 'no'
