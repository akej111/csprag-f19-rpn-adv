#!/usr/bin/env python3

import operator
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def debug(stack, args):
    print(stack)
    print(args)

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result > 0:
            print(colored("Result:", "white", "on_magenta"), colored(result, "white", "on_green"))
        elif result < 0:
            print(colored("Result:", "white", "on_magenta"), colored(result, "white", "on_red"))
        else:
            print(colored("Result:", "white", "on_magenta"), colored(result, "white"))

if __name__ == '__main__':
    main()
