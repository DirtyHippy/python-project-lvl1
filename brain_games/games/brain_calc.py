import random


GAME_RULES = 'What is the result of the expression?'


def make_question():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operation = random.choice('+-*')
    question = "{} {} {}".format(first_number, operation, second_number)
    return question, str(eval(question))
