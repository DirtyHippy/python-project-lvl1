from brain_games import cli
from random import choice


def main():
    user_name = cli.welcome_user('What number is missing in the progression?')
    run_game(user_name)


def run_game(user_name):
    for i in range(0, 3):
        question, correct_answer = make_question()
        user_answer = cli.ask_question(question)
        cli.show_result(user_answer, correct_answer, user_name)
        if user_answer != correct_answer:
            break
    else:
        cli.congratulate(user_name)


def make_question():
    first_number = cli.get_random_number()
    step = cli.get_random_number()
    progression = [str(first_number)]
    for i in range(1, 10):
        next_number = first_number + i * step
        progression.append(str(next_number))
    secret_number = choice(progression)
    question = " ".join(progression)
    question = question.replace(secret_number, '..')
    return question, secret_number


if __name__ == '__main__':
    main()
