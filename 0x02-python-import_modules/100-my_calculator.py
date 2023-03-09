#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, mul, div, sub

    if (len(argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] == '+':
            print("{:d}".format(add(int(argv[1]), int(argv[3]))))
        elif argv[2] == '-':
            print("{:d}".format(sub(int(argv[1]), int(argv[3]))))
        elif argv[2] == '*':
            print("{:d}".format(mul(int(argv[1]), int(argv[3]))))
        elif argv[2] == '/':
            print("{:d}".format(div(int(argv[1]), int(argv[3]))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
