import random
import operator


GAME_RULES = 'What is the result of the expression?'
OPERATIONS = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def make_question():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operation = random.choice(list(OPERATIONS.keys()))
    question = "{} {} {}".format(first_number, operation, second_number)
    correct_answer = OPERATIONS[operation](first_number, second_number)
    return question, str(correct_answer)
