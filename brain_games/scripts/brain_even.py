from brain_games.scripts.brain_games import greet
from brain_games.cli import congratulate, show_result
from random import randint
import prompt


def main():
    user_name = greet()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(user_name)


def game(user_name):
    won = True
    for i in range(0, 3):
        number = ask_question()
        answer = prompt.string('Your answer:')
        if check_answer(answer, number):
            show_result(True, 'yes', 'no', user_name)
        else:
            show_result(False, 'yes', 'no', user_name)
            won = False
            break
    if won:
        congratulate(user_name)


def ask_question():
    random_number = randint(1, 100)
    print('Question: {}'.format(random_number))
    return random_number


def is_even(number):
    return number % 2 == 0


def check_answer(answer, num):
    res = is_even(num)
    return (res and answer == 'yes') or (not res and answer == 'no')


if __name__ == '__main__':
    main()
