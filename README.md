# Data Structures Project

This course required implementing data structures to solve problems. I used Linked Lists, Queues, Priority Queues, and Binary Trees. This work is my own. It is not a tutorial.

### [LRU Cache](./01_lru_cache.py)

Implements Least Recently Used Caching algorithm similar to this [Python functools decorator](https://docs.python.org/3/library/functools.html#functools.lru_cache). My cache tracks the most recently used elements with a Linked List Queue. It refreshes elements in queue in constant O(1) time using a hash map.

### [Find Files](./02_find_files.py) 

Searches recursively for files within a path ending with a suffex parameter. This is easily implemented with `os.walk()` [docs](https://docs.python.org/3.8/library/os.html#os.walk), however the instructions asked to use `os.path.isdir(path)`, `os.path.isfile(path)`, and `os.listdir(path)`.

### [Huffman Coding](./03_huffman_coding.py) 
Uses a priority queue [docs](https://docs.python.org/3/library/asyncio-queue.html#priority-queue) to build a binary search tree (BST). Uses depth first search (DFS) postorder traversal for both encoding and decoding. Decoding method iterates through encoded string, and searches for potential code matches within hashed dictionary.
- [Visualizer](https://people.ok.ubc.ca/ylucet/DS/Huffman.html)
- [Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)

### [Active Directory](./04_active_directory.py)
Recursive solution traverses a user group hierarchy. It determines if a user belongs to a group directly or if their group (recoursively) belongs to a group.

### [blockchain](./05_blockchain.py)
Fun chanlenge to practice linked lists and hashing functions.

### [Union and Intersection of Two Linked Lists](./06_union_intersection.py)
Iterates through linked lists finding union and intersection.
