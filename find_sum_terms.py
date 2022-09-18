"""Coding Problem #1
Given a list of numbers and a number K, return whether any two numbers
from the list add up to k.

Example:
givern [10, 15, 3, 7] and k of 17,
return True since 10 + 7 is 17
"""
from typing import List


def find_sum_terms(array: List[int], k: int) -> str:
    possible_factors: dict[int, int] = dict()
    checked_numbers: dict[int, int] = dict()
    size = len(array)
    found = False

    for i in range(size):
        factor = k - array[i]
        if array[i] in possible_factors or factor in checked_numbers:
            found = True
            f1 = array[i]
            i2 = possible_factors[f1] or checked_numbers[factor]
            f2 = array[i2]
            result = f'[{found}] => {f1} + {f2} = {k}'
            break

        else:
            possible_factors[factor] = i
            checked_numbers[array[i]] = i
    if not found:
        result = f'[{found}] => No two numbers add up to {k}'
    return result


array = [10, -15, 3, 7]
k = -5
print(find_sum_terms(array, k))
