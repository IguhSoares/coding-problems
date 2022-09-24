from __future__ import annotations
from typing import Any, Final


class Node:
    def __init__(self, val: Any) -> Node:
        self.value = val
        self.next: Node|None = None
        self.prev: Node|None = None

    def __str__(self) -> str:
        return f'{self.value}'

    __repr__ = __str__


class DoublyLinkedList:
    def __init__(self) -> DoublyLinkedList:
        self.head: Node|None = None
        self.tail: Node|None = None
        self.length: int = 0

    EMPTY_LIST_MSG: Final[str] = 'Empty List'

    def __str__(self) -> str:
        if not self.head:
            return self.EMPTY_LIST_MSG

        n = self.head
        list_values: str = 'Start'
        for _ in range(self.length):
            list_values += f' -> {n}'
            n = n.next

        return list_values

    __repr__ = __str__

    def append(self, val: Any) -> Any:
        node = Node(val)

        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.prev.next = node
            self.tail = node
        self.length += 1

        return val

    def prepend(self, val: Any) -> Any:
        node = Node(val)

        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
        self.length += 1

        return val

    def pop_wrapper(func):
        def pop(self) -> Any:
            if not self.head:
                raise LookupError(f'{self.EMPTY_LIST_MSG} >> No element to pop')

            if self.length == 1:
                val = self.head.value
                self.head = self.tail = None
            else:
                val = func(self)
            self.length -= 1

            return val
        return pop

    @pop_wrapper
    def pop_last(self) -> Any:
        node = self.tail
        self.tail = node.prev
        self.tail.next = None
        node.prev = None

        return node.value

    @pop_wrapper
    def pop_first(self) -> Any:
        node = self.head
        self.head = node.next
        self.head.prev = None
        node.next = None

        return node.value

    def peek_wrapper(func):
        def peek(self) -> Any:
            if not self.head:
                raise LookupError(f'{self.EMPTY_LIST_MSG} >> No element to peek')

            return func(self)
        return peek

    @peek_wrapper
    def peek_first(self) -> Any:
        return self.head.value

    @peek_wrapper
    def peek_last(self) -> Any:
        return self.tail.value
