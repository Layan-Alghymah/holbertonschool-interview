#!/usr/bin/python3
"""Read HTTP logs and print cumulative statistics."""

import re
import sys


def print_stats(total_size, status_counts):
    """Print total file size and status code counts."""
    print("File size: {}".format(total_size))

    for status in sorted(status_counts):
        print("{}: {}".format(status, status_counts[status]))


def main():
    """Process input lines and update statistics."""
    total_size = 0
    status_counts = {}
    line_count = 0

    pattern = re.compile(
        r'^\S+ - \[[^\]]+\] '
        r'"GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
    )

    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.fullmatch(line.strip())

            if match:
                status = int(match.group(1))
                size = int(match.group(2))

                total_size += size

                if status in valid_codes:
                    status_counts[status] = (
                        status_counts.get(status, 0) + 1
                    )

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        return

    if line_count % 10 != 0:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
