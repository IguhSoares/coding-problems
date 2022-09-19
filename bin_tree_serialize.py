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
    
    while values != []:
        val = values.pop(0)
        
        queue = [root]
        while queue != []:
            node = queue.pop(0)
            if node == -1:
                node = None if val == 'None' else Node(int(val), -1, -1)
                break
            elif node.left == -1:
                node.left = None if val == 'None' else Node(int(val), -1, -1)
                break
            elif node.right == -1:
                node.right = None if val == 'None' else Node(int(val), -1, -1)
                break

            if node != None:
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

    return root

root = Node(16)
array = [1, 7, 8, 32, 25, 21, 3, 64, 55, 43]
# array = [15, 17]
for n in array:
    root.append(n)

print( serialize(root) )
print('\n')
print(serialize(  deserialize(serialize(root))  ))
# tree =   deserialize('16, 1, 32, 0, 7, 25, None, None, None, None, None, None, None')  
# queue = [tree]
# while queue != []:
#     node = queue.pop(0)
#     print(f'Node: {node.value} => left: {  node.left.value if node.left not in [-1, None]  else node.left }')
#     print(f'Node: {node.value} => right: {  node.right.value if node.right not in [-1, None] else node.right }')
#     if type(node.left) == Node:
#         queue.append(node.left)
#     if type(node.right) == Node:
#         queue.append(node.right)
