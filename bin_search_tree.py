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

    def print_tree(self):
        queue = [self]
        while queue != []:
            node = queue.pop(0)
            print(f'Node: {node.value} => left: {  node.left.value if node.left != None else node.left }')
            print(f'Node: {node.value} => right: {  node.right.value if node.right != None else node.right }')
            if type(node.left) == Node:
                queue.append(node.left)
            if type(node.right) == Node:
                queue.append(node.right)
