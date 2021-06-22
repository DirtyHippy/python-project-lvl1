from brain_games import cli
from brain_games.games import brain_prime


def main():
    game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    cli.run_game(brain_prime, game_rules)


def make_question():
    number = cli.get_random_number()
    return number, is_prime(number)


def is_prime(n):
    if n < 2:
        return 'no'
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return 'yes' if d * d > n else 'no'


if __name__ == '__main__':
    main()
