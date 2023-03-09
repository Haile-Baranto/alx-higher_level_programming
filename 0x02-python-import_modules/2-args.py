#!/usr/bin/python3

from sys import argv


def main():
    if (len(argv) - 1) == 1:
        print(f"{len(argv) - 1} argument:")
    elif (len(argv) - 1) == 0:
        print(f"{len(argv) - 1} arguments.")
    else:
        print(f"{len(argv) - 1} arguments:")
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")


if __name__ == "__main__":
    main()
