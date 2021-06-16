#!/usr/bin/env python
import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    
def main():
    greet()
    
    
if __name__ == '__main__':
    main()
