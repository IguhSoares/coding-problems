from typing import List, Tuple


def merge_tuple(left: List[Tuple], right: List[Tuple]) -> List[Tuple]:
    # [(start, end), (start, end)]
    size_L = len(left)
    size_R = len(right)
    result: List[int] = []

    i, j = [0, 0]
    while i < size_L and j < size_R:
        if left[i].end <= right[j].end:
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


def mergesort(array: List[int]) -> List[int]:
    size = len(array)
    if size == 1:
        return array

    left: List[int] = mergesort(array[: size // 2])
    right: List[int] = mergesort(array[size // 2 :])

    return merge_tuple(left, right)
