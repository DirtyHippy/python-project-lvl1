from brain_games import cli
from brain_games.games import brain_even


def main():
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    cli.run_game(brain_even, game_rules)


def make_question():
    number = cli.get_random_number(1, 100)
    return number, is_even(number)


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


if __name__ == '__main__':
    main()
