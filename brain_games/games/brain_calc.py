import random


GAME_RULES = 'What is the result of the expression?'


def make_question():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operation = random.choice('+-*')
    question = "{} {} {}".format(first_number, operation, second_number)
    correct_answer = calc(first_number, second_number, operation)
    return question, str(correct_answer)


def calc(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
