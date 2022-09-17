"""Coding Problem #33

Compute the running median of a squence of numbers.
Given a strem of numbers, print out the median of the list so far on each new element

Example:
Given the sequence [2, 1, 5, 7, 2, 0, 5], should print out:
2
1.5
2
3.5
2
2
2
"""
from typing import List
from shellsort import shellsort


def running_median(array: List[int]) -> None:
    aux: List[int] = []

    for n in array:
        aux.append(n)
        aux = shellsort(aux)

        size = len(aux)
        if size % 2 == 1:
            median = aux[size//2]
        else:
            median = (aux[size//2] + aux[size//2 - 1])/2

        print(f'Median: {median} => List: {aux}')

array = [2, 1, 5, 7, 2, 0, 5]
running_median(array)
print('\n')
array = [13,42,77,45,2,9,26,11,56]
running_median(array)