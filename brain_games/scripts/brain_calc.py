from brain_games import cli


GAMES_COUNT = 3


def main():
    user_name = cli.welcome_user('What is the result of the expression?')
    run_game(user_name)


def run_game(user_name):
    for i in range(0, GAMES_COUNT):
        question, correct_answer = make_question()
        user_answer = cli.ask_question(question)
        cli.show_result(user_answer, correct_answer, user_name)
        if user_answer != correct_answer:
            break
    else:
        cli.congratulate(user_name)


def make_question():
    first_number = cli.get_random_number()
    second_number = cli.get_random_number()
    operation = cli.get_random_operation()
    question = "{} {} {}".format(first_number, operation, second_number)
    return question, str(eval(question))


if __name__ == '__main__':
    main()
