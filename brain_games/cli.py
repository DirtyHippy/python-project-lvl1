import prompt
import random


GAMES_COUNT = 3


def main():
    welcome_user()


def welcome_user(game_rules):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game_rules)
    return user_name


def get_random_number(lower=1, upper=100):
    return random.randint(lower, upper)


def ask_question(question):
    print("Question: {}".format(question))
    answer = prompt.string("Your answer: ")
    return answer


def show_result(user_answer, correct_answer, user_name):
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
            user_answer, correct_answer))
        print("Let's try again, {}!".format(user_name))


def run_game(game_module, game_rules):
    user_name = welcome_user(game_rules)
    for _ in range(GAMES_COUNT):
        question, correct_answer = game_module.make_question()
        user_answer = ask_question(question)
        show_result(user_answer, correct_answer, user_name)
        if user_answer != correct_answer:
            break
    else:
        print("Congratulations, {}!".format(user_name))


if __name__ == '__main__':
    main()
