# LRUCache
An implementation of LRU Cache made for a leetcode problem.

It supports get and put operations, both of which run in O(1) time.

This works by having a hashtable and a linked list. The linked list makes it possible to update and keep track of the least and most recently used items in O(1) time.

parse_test.py was to easily create paste-able code using the leetcode test cases.

### Room for improvement
The implementation works as is, but I could've shortened the code by combining the LRUCache and LRU classes. The LRUCache hashtable could've had the nodes as values for each key.
