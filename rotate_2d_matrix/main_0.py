#!/usr/bin/python3
"""Test matrix rotation."""

rotate_2d_matrix = __import__(
    '0-rotate_2d_matrix'
).rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
