import prompt


def main():
    welcome_user()


def welcome_user(game_rules):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game_rules)
    return user_name


if __name__ == '__main__':
    main()
