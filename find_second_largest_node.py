"""Coding Problem #36
Given the root to a binary search tree, find the second largest node in the tree
"""
from bin_search_tree import Node


def find_second_largest(root: Node) -> Node:
    node = root
    # finds the largest node
    while node.has_right_child():
        node = node.right
    
    if node.has_left_child():
        second_largest = node.left
    else:
        second_largest = node.parent
 
    return second_largest 

root = Node(16)
array = [1, 7, 8, 32, 25, 21, 3, 64, 55, 43]
for n in array:
    root.append(n)

second_largest = find_second_largest(root)
print(second_largest.value)
