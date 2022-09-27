"""Coding Problem #20
Given two singly linked lists that intersect at some point,
    find the intersecting node. The lists are non-cyclical.

Example:
Given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
    return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists)
    and constant space.
"""
from linked_list import Node, SinglyLinkedList


def find_intersection(list_A: SinglyLinkedList, list_B: SinglyLinkedList) -> Node:
    def same_length_intersection_search(list_A: SinglyLinkedList, list_B: SinglyLinkedList):
        # if both lists have the same length
        pointer_A: Node
        pointer_B: Node
        pointer_A, pointer_B = list_A.head, list_B.head
        # walk the list till intersection is found
        # (nodes with the same value are the exact same node object)
        while pointer_A != pointer_B or pointer_A.next != pointer_B.next:
            pointer_A, pointer_B = pointer_A.next, pointer_B.next

        return pointer_A

    if list_A.length == list_B.length:
        return same_length_intersection_search(list_A, list_B)
    else:
        longest, shortest = (list_A, list_B) if list_A.length > list_B.length else (list_B, list_A)
        count = longest.length
        pointer: Node = longest.head
        # walk the longest list untill the number of elements counting from pointer
        # is equal to shortest list length
        while count != shortest.length:
            pointer = pointer.next
            count -= 1

        temp = SinglyLinkedList()
        temp.head = pointer
        return same_length_intersection_search(temp, shortest)
