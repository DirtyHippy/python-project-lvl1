#!/usr/bin/env python
import prompt


def welcome_user(): 
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    return user_name


def main():
    welcome_user()


def congratulate(user_name):
    print("Congratulations, {}!".format(user_name))


def show_result(is_correct, correct_answer, wrong_answer, user_name):
    if is_correct:
        print("Correct!")
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(correct_answer, wrong_answer))
        print("Let's try again, {}!".format(user_name))


if __name__ == '__main__':
    main()
