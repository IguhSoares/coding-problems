"""Coding Problem #8

A unival tree is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
(Leafs count as a unival tree)
"""
from __future__ import annotations

class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.size: int = 1
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None
    
    def has_left_child(self):
        return bool(self.left)

    def has_right_child(self):
        return bool(self.right)

    def append_child(self, value: int) -> Node:
        node = Node(value) 

        def append_to_right():
            self.right = node
            self.right.parent = self

        def append_to_left():
            self.left = node
            self.left.parent = self

        if (not self.has_left_child() or
            self.has_right_child() and self.left.size <= self.right.size):
            append_to_left()
        else:
            append_to_right()

        parent_node = node.parent
        if parent_node != None:
            parent_node.size += 1

            while parent_node.parent != None:
                parent_node.parent.size += 1
                parent_node = parent_node.parent

        return node


def is_unival_tree(root: Node) -> bool:
    if root == None or root.size == 0:
        return True

    if not root.has_left_child() and not root.has_right_child():
        return True

    if root.has_left_child():
        is_left_unival = is_unival_tree(root.left)
        if root.has_right_child():
            if not (is_left_unival and is_unival_tree(root.right)):
                return False
            else: # both children are unival
                return root.value == root.left.value
        else: # no right child, only left child
            return is_left_unival and root.value == root.left.value

    else: # No left child, right child only
        return is_unival_tree(root.right) and root.value == root.right.value

def unival_count(root: Node) -> int:
    if is_unival_tree(root):
        return root.size

    count = 0
    if root.has_left_child:
        count += unival_count(root.left)

    if root.has_right_child:
        count += unival_count(root.right)

    return count

root = Node(0)
root.append_child(1)
root.append_child(0).append_child(1).append_child(1)
root.right.append_child(0)
root.right.left.append_child(1)

print(f'Total unival trees: { unival_count(root) }')

# print(is_unival_tree(root))
# print(is_unival_tree(root.left))
# print(is_unival_tree(root.right))
# print(is_unival_tree(root.right.left))
# print(is_unival_tree(root.right.right))