#!/usr/bin/python3
import sys
import re


def format_each_line():
    pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "([^"]+)" (\d{3}) (\d+)$')
    dictionary = {200: 0, 301: 0, 400: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    total_size = 0
    count = 0
    for line in sys.stdin:
        text = pattern.search(line)
        status_code = text[-2]
        file_size = text[-1]
        total_size += file_size
        for key, value in dictionary.items():
            if key == status_code:
                value += 1
        count += 1
        if count == 10:
            print(f"File size: {total_size}")
            for key, value in dictionary.items():
                print(f"{key}: {value}")
            return format_each_line()
                






    




