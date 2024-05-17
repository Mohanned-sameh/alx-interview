#!/usr/bin/python3
"""Log parsing"""
import sys

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        try:
            status = data[-2]
            if status in status_codes:
                status_codes[status] += 1
            total_size += int(data[-1])
        except Exception:
            pass
        if counter % 10 == 0:
            print("File size: {}".format(total_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
