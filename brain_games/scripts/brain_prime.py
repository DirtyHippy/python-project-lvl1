from brain_games import cli
from random import choice


def main():
    user_name = cli.welcome_user('Answer "yes" if given number is prime. Otherwise answer "no".')
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
    number = cli.get_random_number()
    return number, is_prime(number)


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return 'yes' if d * d > n else 'no'


if __name__ == '__main__':
    main()
