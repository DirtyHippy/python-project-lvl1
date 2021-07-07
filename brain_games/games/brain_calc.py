import random
import operator


GAME_RULES = 'What is the result of the expression?'


def make_question():
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operation = random.choice(list(operations.keys()))
    question = "{} {} {}".format(first_number, operation, second_number)
    correct_answer = operations[operation](first_number, second_number)
    return question, str(correct_answer)
