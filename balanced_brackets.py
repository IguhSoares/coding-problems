"""Coding problem #27
Given a string of round (), curly {}, and square [] open and closing brackets,
return whether the brackets are balanced.

Examples:
-> ([])[]({}) => True (balanced)
-> ([)] or ((() => False (unbalanced)
"""
from typing import Dict, List


def check_brackets_balance(string: str):
    # Tracks the indexes in the string, for each open bracket:
    opening_indexes: Dict[str, List[int]] = {"(": [], "[": [], "{": []}
    length = len(string)

    for i in range(length):
        bracket: str = string[i]
        if bracket in ["(", "[", "{"]:
            opening_indexes[bracket].append(i)
        else: # bracket is a closing bracket
            # opposite gets its opening pair:
            opposite = ["(", "[", "{"][[")", "]", "}"].index(bracket)]
            # List of indexes of the opening bracket:
            opposite_indexes = opening_indexes[opposite]
            
            if opposite_indexes == []:
                # Closing bracket without a opening pair
                return False
            
            # distance is the number of characters between the closing bracket
            #   and the previous corresponding opening bracket
            distance = i - opposite_indexes[-1] - 1
            if distance == 0:
                # The pair is balanced: no characters between
                #   opening and closet brackets
                # Removes corresponding opening bracket from indexes list:
                opposite_indexes.pop()
            elif distance % 2 == 1:
                # Unbalanced: There's a odd number of brackets in between the
                #   current pair of brackets
                return False
            else:
                # Verifies if all the other brackets between the current pair of
                #   brackets are balanced:
                for other_bracket, indexes in opening_indexes.items():
                    if other_bracket != bracket and indexes != []:
                        if opposite_indexes[-1] < indexes[-1] < i:
                            # Unbalanced: there's a opening bracket whithout
                            # closing between the current pair of brackets
                            return False
                # Balanced pair
                # Removes corresponding opening bracket from indexes list:
                opposite_indexes.pop()

    for indexes in opening_indexes.values():
        # Verifies whether there are any opening brackets left without closing:
        if indexes != []:
            return False

    return True


print(f"[([{()}])]: {check_brackets_balance('[([{()}])]')}")
print("[([()}])]: " + f"{ check_brackets_balance('[([()}])]') }")
print("[([{((}])]: " + f"{ check_brackets_balance('[([{((}])]') }")
print("[([{()()}])]: " + f"{ check_brackets_balance('[([{()()}])]') }")
print("[([{()(}])]: " + f"{ check_brackets_balance('[([{()(}])]') }")
print("[{[[[()]]]}]: " + f"{ check_brackets_balance('[{[[[()]]]}]') }")
print("(((((): " + f"{ check_brackets_balance('((((()') }")
