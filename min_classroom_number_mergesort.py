# Coding Problem #21
# Given an array of time intervals (start, end) for classrom lectures
# find the minimun number of rooms required
#
# Example: [(30, 75), (0, 50), (60,150)] -> return 2
from typing import List, NamedTuple, Tuple
from collections import namedtuple
from mergesort import mergesort

Duration: NamedTuple = namedtuple("Duration", "start end")


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

def min_classroom_number():
    time_intervals = [
        Duration(30, 75),
        Duration(80, 110),
        Duration(65, 150),
        Duration(15, 65),
        Duration(85, 130),
        Duration(0, 50),
        Duration(60, 150),
    ]

    """
    Worst case scenario:
    all durations overlapping, so number of rooms (k) is
    equal to the number of durations (n)
    In this case, the complexity will be O(n²)
    """
    # time_intervals = [ # Worst case scenario example
    #     Duration(30, 75),
    #     Duration(49, 110),
    #     Duration(40, 150),
    #     Duration(15, 65),
    #     Duration(49, 130),
    #     Duration(0, 50),
    #     Duration(40, 150),
    # ]

    possible_classes: List[Duration] = mergesort(time_intervals, merge_tuple)  # O(n*logn)

    rooms: List[List[Duration]] = []

    while bool(possible_classes):
        appended = False
        if rooms != []:
            for room in rooms:  # O(k*n), k = number of rooms
                last_class = room[-1]
                min_start_time = None
                for duration in possible_classes:  # O(n)
                    if not bool(min_start_time):
                        if last_class.end <= duration.start:
                            min_start_time = duration
                    else:
                        if last_class.end <= duration.start < min_start_time.start:
                            min_start_time = duration

                if bool(min_start_time):
                    room.append(min_start_time)
                    possible_classes.remove(min_start_time)  # O(n)
                    appended = True

        if not appended:
            rooms.append([possible_classes.pop(0)])

    print(f"=> { len(rooms) } classrooms:")
    i = 0
    for room in rooms:  # O(k*n)
        i += 1
        classes = f"=> #{i}"
        for duration in room:
            classes += f" -> ({duration.start}, {duration.end})"
        print(classes)


min_classroom_number()
