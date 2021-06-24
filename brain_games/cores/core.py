from brain_games import cli
import prompt

GAMES_COUNT = 3


def run(game_module):
    user_name = cli.welcome_user(game_module.GAME_RULES)
    for _ in range(GAMES_COUNT):
        question, correct_answer = game_module.make_question()
        user_answer = ask_question(question)
        show_result(user_answer, correct_answer, user_name)
        if user_answer != correct_answer:
            break
    else:
        print("Congratulations, {}!".format(user_name))


def ask_question(question):
    print("Question: {}".format(question))
    answer = prompt.string("Your answer: ")
    return answer


def show_result(user_answer, correct_answer, user_name):
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
            user_answer, correct_answer))
        print("Let's try again, {}!".format(user_name))
