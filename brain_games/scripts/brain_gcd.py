from brain_games import cli


def main():
    user_name = cli.welcome_user('Find the greatest common divisor of given numbers.')
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
    first_number = cli.get_random_number()
    second_number = cli.get_random_number()
    return "{} {}".format(first_number, second_number), str(gcd(first_number, second_number))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    main()
