from brain_games.scripts.brain_games import greet
from brain_games.cli import congratulate, show_result
from random import randint, choice
import prompt


def main():
    greet()
    print('What is the result of the expression?')
    game(user_name)


def main():
    user_name = greet()
    print('What is the result of the expression?')
    game(user_name)


def game(user_name):
    won = True
    for i in range(0, 3):
        number = ask_question()
        answer = prompt.string('Your answer:')
        if check_answer(answer, number):
            show_result(True, answer, number, user_name)
        else:
            show_result(False, answer, number, user_name)
            won = False
            break
    if won:
        congratulate(user_name)


def ask_question():
    operation = choice('+-*')
    expression = str(randint(1, 100)) + operation + str(randint(1, 100))
    print('Question: {}'.format(expression))
    return eval(expression)


def check_answer(answer, num):
    return int(answer) == int(num)


if __name__ == '__main__':
    main()
