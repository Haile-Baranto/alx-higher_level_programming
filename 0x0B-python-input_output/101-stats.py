#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code

Input format: <IP Address> - [<date>] "GET /projects/260
HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints the statistics since the beginning.
"""

import sys
from collections import defaultdict


def print_status():
    """
    Prints the status of requests based on the input.
    Computes metrics such as total file size and number
    of lines by status code.
    """
    counter = 0
    size = 0
    file_size = 0
    status_counts = defaultdict(int)

    for line in sys.stdin:
        line_data = line.split()
        try:
            file_size = int(line_data[-1])
            status_code = line_data[-2]
            size += file_size
            status_counts[status_code] += 1
        except (IndexError, ValueError):
            continue

        counter += 1
        if counter == 10:
            print_metrics(size, status_counts)
            counter = 0

    if counter != 0:
        print_metrics(size, status_counts)


def print_metrics(size, status_counts):
    """
    Prints the metrics: total file size and number of lines by status code.
    """
    print("File size: {}".format(size))
    for status_code in sorted(status_counts):
        count = status_counts[status_code]
        if count > 0:
            print("{}: {}".format(status_code, count))


if __name__ == "__main__":
    print_status()
