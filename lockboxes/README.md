# Lockboxes

## Description

This project focuses on solving the **Lockboxes** problem using Python.

Given a number of locked boxes, each box may contain keys to other boxes. The goal is to determine whether all the boxes can be opened starting from the first box, which is always unlocked.

Each box is numbered sequentially from `0` to `n - 1`, and a key with the same number as a box can unlock that box.

## Requirements

- Python 3.4.3
- Ubuntu 14.04 LTS
- Code must follow PEP 8 style
- All files must be executable
- All files must end with a new line
- The first line of Python files must be:

```python
#!/usr/bin/python3
```

## Function

### `canUnlockAll(boxes)`

Determines whether all boxes can be opened.

**Arguments:**

- `boxes`: A list of lists, where each inner list contains keys to other boxes.

**Returns:**

- `True` if all boxes can be opened.
- `False` if one or more boxes cannot be opened.

## Example

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
```

Output:

```text
True
```

Files

0-lockboxes.py — Contains the implementation of the canUnlockAll function.

README.md — Project documentation.
