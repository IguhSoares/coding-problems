"""Coding Problem #16
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

-> record(order_id): adds the order_id to the log

-> get_last(i): gets the ith last element from the log.
    i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""
from linked_list import DoublyLinkedList


class Log(DoublyLinkedList):
    def __init__(self) -> DoublyLinkedList:
        super().__init__()

    def record(self, order_id: int) -> None:
        self.append(order_id)

    def get_last(self, i: int) -> int:
        if i > self.length:
            raise LookupError(f'Only {self.length} logs recorded')

        node = self.tail
        for _ in range(1,i):
            node = node.prev

        return node.value
