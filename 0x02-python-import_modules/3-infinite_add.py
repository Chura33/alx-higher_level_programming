#!/usr/bin/python3


if __name__ == "__main__":

    """Print the addition of all arguments."""

    from sys import argv
    total = 0
    for i in range(len(argv) - 1):
        total += int(argv[i + 1])
    print("{}".format(total))
