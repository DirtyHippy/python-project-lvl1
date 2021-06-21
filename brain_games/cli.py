import prompt
from random import choice, randint


def main():
    welcome_user()


def welcome_user(game_rules):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game_rules)
    return user_name


def get_random_number():
    return randint(1, 100)


def get_random_operation():
    return choice('+-*')


def ask_question(question):
    print("Question: {}".format(question))
    answer = prompt.string("Your answer: ")
    return answer


def congratulate(user_name):
    print("Congratulations, {}!".format(user_name))


def show_result(user_answer, correct_answer, user_name):
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
            user_answer, correct_answer))
        print("Let's try again, {}!".format(user_name))


if __name__ == '__main__':
    main()
