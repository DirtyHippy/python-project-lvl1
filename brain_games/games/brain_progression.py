from brain_games import cli
import random
from brain_games.games import brain_progression


def main():
    game_rules = 'What number is missing in the progression?'
    cli.run_game(brain_progression, game_rules)


def make_question():
    first_number = cli.get_random_number(1, 100)
    step = cli.get_random_number(1, 10)
    progression = []
    for i in range(10):
        next_number = first_number + i * step
        progression.append(str(next_number))
    secret_number_index = random.randint(0, len(progression) - 1)
    secret_number = progression[secret_number_index]
    progression[secret_number_index] = '..'
    question = " ".join(progression)
    return question, secret_number


if __name__ == '__main__':
    main()
