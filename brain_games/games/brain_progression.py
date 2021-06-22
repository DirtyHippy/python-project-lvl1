from brain_games import cli
from random import randint
from brain_games.games import brain_progression


def main():
    game_rules = 'What number is missing in the progression?'
    cli.run_game(brain_progression, game_rules)


def make_question():
    first_number = cli.get_random_number()
    step = cli.get_random_number()
    progression = [str(first_number)]
    for i in range(1, 10):
        next_number = first_number + i * step
        progression.append(str(next_number))
    secret_number_index = randint(0, len(progression) - 1)
    secret_number = progression[secret_number_index]
    progression[secret_number_index] = '..'
    question = " ".join(progression)
    return question, secret_number


if __name__ == '__main__':
    main()
