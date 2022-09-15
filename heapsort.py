from typing import List

"""Given an index i from the heap list, returns index of the parent node"""
def get_parent(i: int) -> int:
    if i == 0:
        parent = -1
    elif i in [1,2]:
        parent = 0
    else:
        parent = (i-1)//2

    return parent

"""Builds a max heap from an unsorted list"""
def max_heap(array: List[int]) -> List[int]:
    size = len(array)

    for i in range(size-1, 0, -1): # O(n*logn)
        parent = get_parent(i)

        if array[i] > array[parent]:
            # if greater than parent node, swap them:
            array[i], array[parent] = array[parent], array[i]

        # if it's not a leaf node (i >= size//2)
        if i < size//2:
            # reheap its parent:
            array = heapify(array, start=parent) # O(logn)

    return array

"""Given an array where the child's nodes of start are a max heap,
    puts the greater element in the start index, making a max heap
    with the list begining in start index
"""
def heapify(array: List[int], size: int=-1, start: int=0) -> List[int]:
    if size == -1:
        # default value for optional argument:
        size = len(array)

    # it's not necessary to heapify leaf nodes (i >= size//2)
    for i in range(start, size//2):
        # left child of i:
        child = 2*i + 1
        
        # if right child exists and greater than left child
        if child + 1 < size and array[child] < array[child + 1]:
            # child == index of i's greatest child
            child += 1
        
        # if i is less than its greatest child
        if array[i] < array[child]:
            # swap them:
            array[i], array[child] = array[child], array[i] 

    return array

"""Sorts an unsorted list in ascending order"""
def heapsort(array: List[int]) -> List[int]:
    array = max_heap(array)
    size = len(array)

    for i in range(0, size):
        last = -1-i # index number counting from the end towards the begining
        
        # because it's a max heap, array[0] is the greatest value in the list
        # swap it with the last unsorted element
        # (from index size-1-i to size-1 the list is already sorted)
        array[last], array[0] = array[0], array[last]
        # after the swap, rebuilds the max heap:
        array = heapify(array, size - 1 - i)

    return array

array = [84, 14, 86, 73, 32, 79, 8, 98, 11, 44, 50, 88, 71, 23, 67, 44, 42, 65, 8, 92, 29, 17, 32, 31, 30, 33, 67, 28, 64, 54, 77, 82, 49, 68, 67, 0, 32, 2, 27, 13, 22, 12, 97, 86, 29, 16, 7, 52, 80, 79, 31, 71, 41, 2, 92, 62, 31, 52, 74, 17, 89, 10, 25, 65, 74, 34, 5, 12, 74, 33, 8, 83, 29, 18, 98, 45, 20, 82, 73, 89, 34, 47, 65, 22, 44, 87, 46, 20, 71, 35, 1, 3, 0, 9, 82, 10, 23, 72, 53, 60]
print(heapsort(array))
print('\n')

array = [84, 14, 86, 73, 32, 79, 8, 98, 11, 44, 50, 88, 71, 23, 67, 44, 42, 65]
print(heapsort(array))
print('\n')

array = [42,13,0,1,7,23,18]
print(heapsort(array))
print('\n')

array = [98,87,72,80,73,70,67]
print(heapsort(array))
print('\n')

array = [13,42,1,7,23,0,18]
print(heapsort(array))
