from brain_games import cli


def main():
    user_name = cli.welcome_user('What is the result of the expression?')
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
    question = str(cli.get_random_number()) + cli.get_random_operation() + str(cli.get_random_number())
    return question, str(eval(question))


if __name__ == '__main__':
    main()
