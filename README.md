# Python List Operations Example

This repository contains a simple Python script, `my_list.py`, that demonstrates basic list operations in Python. The script is intended for beginners who want to learn how to work with lists, including creating, modifying, and querying lists.

## Features
- Create an empty list
- Append elements to a list
- Insert an element at a specific position
- Extend a list with another list
- Remove the last element from a list
- Sort the list in ascending order
- Find the index of a specific value
- Print the list and its properties at each step

## File Overview
- **my_list.py**: The main script that demonstrates the above list operations with explanatory print statements.

## How to Run
1. Make sure you have Python installed (version 3.x recommended).
2. Clone or download this repository.
3. Open a terminal or command prompt in the project directory.
4. Run the script using:
   ```bash
   python my_list.py
   ```

You will see output in the terminal showing each step of the list manipulation process, along with the current state of the list and its properties.

## Example Output
```
Empty list created: []
Type of my_list: <class 'list'>
Length of my_list: 0

After appending elements: [10, 20, 30, 40]
Length of my_list after appending: 4

After inserting 15 at second position: [10, 15, 20, 30, 40]
Length of my_list after inserting: 5

After extending with [50, 60, 70]: [10, 15, 20, 30, 40, 50, 60, 70]
Length of my_list after extending: 8

After removing the last element: [10, 15, 20, 30, 40, 50, 60]
Removed element: 70
Length of my_list after removing: 7

After sorting in ascending order: [10, 15, 20, 30, 40, 50, 60]
Length of my_list after sorting: 7

Index of value 30: 3
Value at index 3 : 30
```

## License
This project is open source and free to use for educational purposes.