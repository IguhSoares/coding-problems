from typing import Callable, List


def merge(left: List[int], right: List[int]) -> List[int]:
    size_L = len(left)
    size_R = len(right)
    result: List[int] = []

    i, j = [0, 0]
    while i < size_L and j < size_R:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < size_L:
        result.append(left[i])
        i += 1

    while j < size_R:
        result.append(right[j])
        j += 1

    return result


def mergesort(array: List[int], merge_func: Callable[ [List, List], List ] = None) -> List[int]:
    size = len(array)
    if size == 1:
        return array

    left: List[int] = mergesort(array[: size // 2])
    right: List[int] = mergesort(array[size // 2 :])


    return merge_func(left, right) if bool(merge_func) else merge(left, right)
