from brain_games import cli
from brain_games.games import brain_calc
import random


def main():
    game_rules = 'What is the result of the expression?'
    cli.run_game(brain_calc, game_rules)


def make_question():
    first_number = cli.get_random_number(1, 10)
    second_number = cli.get_random_number(1, 10)
    operation = random.choice('+-*')
    question = "{} {} {}".format(first_number, operation, second_number)
    return question, str(eval(question))


if __name__ == '__main__':
    main()
