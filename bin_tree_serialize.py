"""Coding Problem #3
Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree
"""
from typing import Any, List
from bin_search_tree import Node


def serialize(root: Node) -> str:
    queue: List[Node] = [root]
    result: List[Any] = [str(root.value)]

    while queue != []:
        node = queue.pop(0)

        if node.has_left_child():
            result.append(str( node.left.value ))
            queue.append(node.left)
        else:
            result.append(str(None))

        if node.has_right_child():
            result.append(str( node.right.value ))
            queue.append(node.right)
        else:
            result.append(str( None ))
    
    return ', '.join(result)

def deserialize(s: str) -> Node:
    values: List[Any] = s.split(', ')
    root: Node = Node(int( values.pop(0) ), -1, -1)
    
    queue = [root]
    while queue != []:
        node = queue.pop(0)
        val = values.pop(0)

        if node == -1:
            node = None if val == 'None' else Node(int(val), -1, -1)
        else:
            if node.left == -1:
                node.left = None if val == 'None' else Node(int(val), -1, -1)
            if node.right == -1:
                val = values.pop(0)
                node.right = None if val == 'None' else Node(int(val), -1, -1)
        
        if node != None:
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    return root

root = Node(16)
array = [1, 7, 8, 32, 25, 21, 3, 64, 55, 43]
for n in array:
    root.append(n)

tree_to_str = serialize(root)
print(f'Serialize:\n {type(tree_to_str)} -> {tree_to_str}\n')
tree = deserialize(tree_to_str)
print(f'Deserialize:\n{type(tree)}')
tree.print_tree()
