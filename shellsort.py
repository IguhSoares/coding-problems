from typing import List


def shellsort(array: List[int]) -> List[int]:
    size = len(array)

    """Using a subset of Pratt's gap sequence"""
    p, q = 0, 0
    gap_sequence: List[int] = [1]
    while True:
        if p == q:
            p += 1
        else:
            q += 1

        gap = (2**p)*(3**q)
        if gap > size:
            break
        gap_sequence.append(gap)

    for gap in gap_sequence[::-1]:
        i = gap
        while i < size:
            j = i
            while j >= gap and array[j - gap] > array[j]:
                array[j - gap], array[j] = array[j], array[j - gap]
                j -= gap
            i += 1
    
    return array
