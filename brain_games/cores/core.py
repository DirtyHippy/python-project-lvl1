from brain_games import cli
import prompt

GAMES_COUNT = 3


def run(game_module):
    user_name = cli.welcome_user(game_module.GAME_RULES)
    for _ in range(GAMES_COUNT):
        question, correct_answer = game_module.make_question()
        print("Question: {}".format(question))
        user_answer = prompt.string("Your answer: ")
        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                user_answer, correct_answer))
            print("Let's try again, {}!".format(user_name))
            break
        else:
            print("Correct!")
    else:
        print("Congratulations, {}!".format(user_name))
