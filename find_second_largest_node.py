"""Coding Problem #36
Given the root to a binary search tree, find the second largest node in the tree
"""
from __future__ import annotations


class Node():
    def __init__(self, value, left: Node=None, right: Node=None):
        self.value = value
        self.left = left
        self.right = right 
        self.parent: Node = None

    def has_left_child(self) -> bool:
        return bool(self.left)

    def has_right_child(self) -> bool:
        return bool(self.right)


    def append(self, value) -> Node:
        def append_to(child: str, value) -> Node:
            if child not in ['left', 'right']:
                raise f'Invalid child: {child}'

            new_node = Node(value)
            new_node.parent = self
            setattr(self, child, new_node)

            return new_node

        if value <= self.value:
            if not self.has_left_child():
                node = append_to('left', value)
            else:
                node = self.left.append(value)
        else:
            if not self.has_right_child():
                node = append_to('right', value)
            else:
                node = self.right.append(value)
        
        return node


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
