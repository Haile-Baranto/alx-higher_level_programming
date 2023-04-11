#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

lines_read = 0
file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for i in range(10000):
        sleep(random.random())
        sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
            random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)
        ))
        sys.stdout.flush()

        lines_read += 1

        try:
            line = input()
        except KeyboardInterrupt:
            break

        file_size += int(line.split()[-1])

        if line.split()[7] in status_codes:
            status_codes[line.split()[7]] += 1

        if lines_read % 10 == 0:
            print("File size: {}".format(file_size))
            for k, v in sorted(status_codes.items()):
                if v != 0:
                    print("{}: {}".format(k, v))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))
