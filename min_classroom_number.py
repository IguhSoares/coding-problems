"""Coding Problem #21

Given an array of time intervals (start, end) for classrom lectures
find the minimun number of rooms required

Example: [(30, 75), (0, 50), (60,150)] -> return 2
"""
from typing import List, NamedTuple
from mergesort import mergesort

class Duration(NamedTuple):
    start: int
    end: int

"""Custom comparisson function passed to mergesort()"""
def compare_tuple(tuple_1: Duration, tuple_2: Duration) -> int:
    return tuple_1.end - tuple_2.end

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
    all durations overlapping, and number of rooms (k) is
    equal to the number of durations (n)
    In this case, the time complexity will be O(n²)
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

    # Sorts all time intervals by end time:
    possible_classes: List[Duration] = mergesort(time_intervals, compare_tuple)  # O(n*logn)

    rooms: List[List[Duration]] = []

    while bool(possible_classes):
        # Tracks whether the time interval was appended to a room:
        appended: bool = False
        if rooms != []:
            for room in rooms:  # O(k*n), k = number of rooms
                # Gets the duration of the last class in this room:
                last_class = room[-1]
                min_start_time = None

                # Finds, if it exists, the time interval with the minimun start time
                #   that starts after the last class in the room:
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
        # If didn't find a room to append this time interval, appends it to a new room:
        if not appended:
            rooms.append([possible_classes.pop(0)])

    return rooms

def print_rooms(rooms: List[List[Duration]]) -> None:
    print(f"=> { len(rooms) } classrooms:")
    i = 0
    for room in rooms:  # O(k*n)
        i += 1
        classes = f"=> #{i}"
        for duration in room:
            classes += f" -> ({duration.start}, {duration.end})"
        print(classes)


print_rooms(min_classroom_number())
