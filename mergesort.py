from typing import Any, Callable, List


"""Default comparisson function"""
def compare_int(i: int, j: int) -> int:
    return i - j

def merge(left: List[int], right: List[int], comparisson_func: Callable[[Any, Any], int] = compare_int) -> List[int]:
    size_L = len(left)
    size_R = len(right)
    result: List[int] = []

    i, j = [0, 0]
    while i < size_L and j < size_R:
        if comparisson_func(left[i], right[j]) <= 0:
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


def mergesort(array: List[int], compare_func: Callable[ [Any, Any], int ] = compare_int) -> List[int]:
    size = len(array)
    if size == 1:
        return array

    left: List[int] = mergesort(array[: size // 2], compare_func)
    right: List[int] = mergesort(array[size // 2 :], compare_func)

    return merge(left, right, compare_func) 
