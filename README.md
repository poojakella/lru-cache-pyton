#LRU Cache in python

## Project Description

This project implements a Least Recently Used (LRU) Cache using Python.
The cache stores key-value pairs and automatically removes the least recently used item when the cache reaches its capacity.

## Features

- Implements LRU Cache from scratch using Python
- Supports `put()` and `get()` operations
- Automatically removes the least recently used item when the cache is full
- Tracks cache hits and cache misses
- Calculates cache hit rate
- Displays the current cache and usage order
- Provides an interactive command-line interface 

## How LRU Works

The cache has a fixed capacity. Each item has a key and a value.

- When an item is added using `put()`, it becomes the most recently used item.
- When an item is accessed using `get()`, it is moved to the most recently used position.
- When the cache is full and a new item is added, the least recently used item is removed.
- The cache keeps track of hits and misses to calculate the hit rate.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Dictionary
- List
- Command-Line Interface (CLI)

## How to Run

1. Clone or download the project.
2. Open the project folder in VS Code.
3. Run `main.py`.
4. Enter the cache capacity when prompted.
5. Use the menu to perform `put`, `get`, and display operations.

### Example

```text
Enter cache capacity: 3

===== LRU CACHE =====
1. Put
2. Get
3. Display Cache
4. Exit

## Project Structure

```text
LRU-Cache-Project/
│
├── lru_cache.py
├── main.py
└── README.md

## Future Enhancements

- Add a graphical user interface (GUI)
- Add persistent cache storage
- Add unit tests
- Improve cache performance using a doubly linked list and hash map

## Author

Kella Naga Poojitha