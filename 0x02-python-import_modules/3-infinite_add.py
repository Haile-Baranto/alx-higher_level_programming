#!/usr/bin/python3

from sys import argv


def main():
    sum = 0
    for i in range(1, len(argv)):
        number = int(argv[i])
        sum += number
    print(sum)


if __name__ == "__main__":
    main()
