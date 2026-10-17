#!/usr/bin/python3
"""Parse HTTP logs and print cumulative statistics."""

import re
import sys


def print_stats(total_size, status_counts):
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))

    for status in sorted(status_counts):
        print("{}: {}".format(status, status_counts[status]))


def main():
    """Read log lines and calculate statistics."""
    total_size = 0
    status_counts = {}
    line_count = 0
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}

    pattern = re.compile(
        r'^\S+ - \[[^\]]+\] '
        r'"GET /projects/260 HTTP/1\.1" '
        r'(\S+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.fullmatch(line.strip())

            if match:
                status_text, size_text = match.groups()
                total_size += int(size_text)

                try:
                    status = int(status_text)
                    if status in valid_codes:
                        status_counts[status] = (
                            status_counts.get(status, 0) + 1
                        )
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        return

    if line_count == 0 or line_count % 10 != 0:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
