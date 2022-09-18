"""Coding Problem #37

The power set is the set of all its subsets.
Write a function that, given a set, generates its power set.

Example:
Given the set {1, 2, 3}, it should return:
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
"""
from typing import List, Set
from mergesort import mergesort


"""Pretty prints frozenset instances"""
class my_set(frozenset):
    def __str__(self):
        return '{' + f'{", ".join([str(e) for e in self])}' + '}'

    def __repr__(self):
        return '{' + f'{", ".join([str(e) for e in self])}' + '}'


"""Returns a set containing all the subsets of entry_set"""
def power_set_of(entry_set: Set[int]) -> Set[my_set]:
    n = len(entry_set)

    # list with the elements in the entry_set
    elements: List[my_set] = []
    power_set = set()
    # An empty set is a subset of any set
    power_set.add(my_set([]))
    for e in entry_set:
        # each element in entry_set will be converted to a set and stored in elements
        elements.append(my_set([e]))
        power_set.add(my_set([e]))

    # queue to store subsets that will be used to generate other subsets
    queue = [e for e in elements]
    
    # for each element in temp, performs a union with the element in elements
    while queue != []:
        element = queue.pop(0)
        i = 0
        while i < n-1:
            j = i + 1
            # will only join sets wich their intersection is a empty set 
            if len(element & elements[j]) == 0:
                new_element = my_set( element | elements[j] )
                power_set.add(new_element)
                queue.append(new_element)
            i += 1

    return power_set

def print_subsets(set: Set):
    """Comparisson function to mergesort the subsets to print"""
    def compare_sets(set_1: my_set, set_2: my_set) -> int:
        return len(set_1) - len(set_2)

    print(f'=> {len(set)} subsets:')
    print('\n'.join(mergesort( [str( e ) for e in set], compare_sets )))

print_subsets( power_set_of(set([1, 2, 3, 4])) )

