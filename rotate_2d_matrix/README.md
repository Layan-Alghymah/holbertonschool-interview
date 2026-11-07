# Rotate 2D Matrix

## Description
This project implements a Python function that rotates an `n x n` 2D matrix 90 degrees clockwise.

The rotation is performed **in-place**, meaning the original matrix is modified without creating a new matrix.

## Requirements
- Python 3.4.3
- Ubuntu 14.04 LTS
- PEP 8 style
- No external modules allowed

## Files
- `0-rotate_2d_matrix.py`: Contains the function to rotate a 2D matrix.

## Usage

```python
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
```

## Expected Output

```text
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Algorithm
1. Transpose the matrix by swapping rows and columns.
2. Reverse each row to complete the 90-degree clockwise rotation.

## Complexity
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
