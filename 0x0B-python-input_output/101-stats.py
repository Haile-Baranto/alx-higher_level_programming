#!/usr/bin/python3
import sys
import signal


def print_statistics(file_size, status_codes):
    """
    Print the computed statistics.

    Args:
        file_size (int): The total file size.
        status_codes (dict): The dictionary containing
        the count of each status code.

    """
    print("Total file size: {}".format(file_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        count = status_codes[code]
        print("{}: {}".format(code, count))


def signal_handler(signal, frame):
    """
    Signal handler for keyboard interruption.

    Args:
        signal: The signal number.
        frame: The current stack frame.

    """
    print_statistics(file_size, status_codes)
    sys.exit(0)


def compute_metrics():
    """
    Read stdin line by line and compute metrics.

    Metrics:
    - Total file size: Sum of all file sizes.
    - Number of lines by status code: Count of each status code.

    """
    lines_count = 0
    file_size = 0
    status_codes = {}

    # Set up the signal handler for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            lines_count += 1
            tokens = line.strip().split()
            if len(tokens) >= 9:
                file_size += int(tokens[-1])
                code = tokens[-2]
                if code in status_codes:
                    status_codes[code] += 1
                else:
                    status_codes[code] = 1

            if lines_count % 10 == 0:
                print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_statistics(file_size, status_codes)


if __name__ == "__main__":
    compute_metrics()
