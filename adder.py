#!/usr/bin/env python3


def adder():
    """ This REPL adds numbers. To exit, enter 0.

        The prompt displays an incrementing index.
    """
    total = 0
    index = 1
    print('Enter 0 to quit.')
    while True:
        try:
            text = input(f'[{index}] ')
        except EOFError:  # no more inputs
            break
        if text == '0':  # exit REPL
            break
        try:
            addend = float(text)
        except ValueError:
            print('Please type numbers.')
            continue
        total += addend
        print(total)
        index += 1


if __name__ == '__main__':
    adder()
