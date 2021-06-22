from brain_games import cli
from brain_games.games import brain_calc


def main():
    game_rules = 'What is the result of the expression?'
    cli.run_game(brain_calc, game_rules)


def make_question():
    first_number = cli.get_random_number()
    second_number = cli.get_random_number()
    operation = cli.get_random_operation()
    question = "{} {} {}".format(first_number, operation, second_number)
    return question, str(eval(question))


if __name__ == '__main__':
    main()
