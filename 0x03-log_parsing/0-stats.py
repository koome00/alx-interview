#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys
import re


def format_each_line():
    """
    uses regular expression to match and then give
    metrics
    """
    pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "([^"]+)" (\d{3}) (\d+)$')
    dictionary = {200: 0, 301: 0, 400: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    total_size = 0
    count = 0
    try:
        for line in sys.stdin:
            text = pattern.search(line)
            if text:
                status_code = int(text.group(4))
                file_size = int(text.group(5))
                total_size += file_size
                if status_code in dictionary:
                    dictionary[status_code] += 1
                    count += 1
            if count % 10 == 0:
                print(f"File size: {total_size}")
                for key, value in dictionary.items():
                    if value != 0:
                        print(f"{key}: {value}")
    except KeyboardInterrupt:
        pass
    finally:
        print(f"File size: {total_size}")
        for key, value in dictionary.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    format_each_line()
