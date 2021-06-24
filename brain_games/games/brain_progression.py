import random


GAME_RULES = 'What number is missing in the progression?'


def make_question():
    first_number = random.randint(1, 100)
    step = random.randint(1, 10)
    progression = []
    for i in range(10):
        next_number = first_number + i * step
        progression.append(str(next_number))
    secret_number_index = random.randint(0, len(progression) - 1)
    secret_number = progression[secret_number_index]
    progression[secret_number_index] = '..'
    question = " ".join(progression)
    return question, secret_number
