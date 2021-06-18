from brain_games.scripts.brain_games import greet
from random import randint
import prompt


def main():
    greet()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    won = True
    for i in range(0, 3):
        number = guess_number()
        answer = prompt.string('Your answer:')
        if check_answer(answer, number):
            show_result(True)
        else:
            show_result(False)
            won = False
            break
    if won:
        congratulate()


def guess_number():
    random_number = randint(1, 100)
    print('Question: {}'.format(random_number))
    return random_number


def show_result(is_correct):
    if is_correct:
        print("Correct!")
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again, Bill!")


def is_even(number):
    return number % 2 == 0


def check_answer(answer, num):
    is_even = is_even(num)
    return (is_even and answer == 'yes') or (not is_even and answer == 'no')


def congratulate():
    print("Congratulations, Sam!")


if __name__ == '__main__':
    main()
