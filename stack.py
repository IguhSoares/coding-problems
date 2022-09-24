"""Coding Problem #43
Implement a stack that has the following methods:

-> push(val), which pushes an element onto the stack

-> pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return null.

-> max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time
"""
from __future__ import annotations
from typing import Any, Final


class Node:
    def __init__(self, val: Any) -> Node:
        self.value = val
        self.prev: Node|None = None
        self._current_max_val: int|None = None

    def __str__(self) -> str:
        return f'{self.value}'

    __repr__ = __str__


class Stack:
    def __init__(self) -> Stack:
        self.top: Node|None = None
        self.length: int = 0

    def push(self, val: Any) -> Any:
        node = Node(val)

        max_val = val
        if self.top:
            node.prev = self.top
            if val < node.prev._current_max_val:
                max_val = node.prev._current_max_val

        node._current_max_val = max_val
        self.top = node
        self.length += 1

        return val

    EMPTY_STACK_MSG: Final[str] = 'Stack is Empty' 

    def pop(self) -> Any:
        if not self.top:
            raise LookupError(f'{self.EMPTY_STACK_MSG}: no element to pop.')

        node = self.top
        self.top = node.prev
        self.length -= 1
        node.prev = None

        return node.value

    def peek(self) -> Any:
        if not self.top:
            raise LookupError(f'{self.EMPTY_STACK_MSG}: no element to peek.')

        return self.top.value

    def max(self) -> Any:
        if not self.top:
            raise LookupError(self.EMPTY_STACK_MSG)

        return self.top._current_max_val

    def __str__(self) -> str:
        if not self.top:
            return self.EMPTY_STACK_MSG

        stack: str = 'Top'
        node: Node = self.top
        for i in range(self.length):
            stack += f' -> {node}'
            node = node.prev

        return stack

    __repr__ = __str__
