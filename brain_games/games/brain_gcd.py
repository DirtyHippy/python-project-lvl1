from brain_games import cli
from brain_games.games import brain_gcd


def main():
    game_rules = 'Find the greatest common divisor of given numbers.'
    cli.run_game(brain_gcd, game_rules)


def make_question():
    first_number = cli.get_random_number()
    second_number = cli.get_random_number()
    question = "{} {}".format(first_number, second_number)
    correct_answer = str(gcd(first_number, second_number))
    return question, correct_answer


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    main()
