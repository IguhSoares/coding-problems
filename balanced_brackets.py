#  Coding problem #27
#  Given a string of round (), curly {}, and square [] open and closing brackets,
#  return whether the brackets are balanced.
#  -> ([])[]({}) => True (balanced)
#  -> ([)] or ((() => False (unbalanced)
def check_brackets_balance(string):
    open_indexes = {"(": [], "[": [], "{": []}
    length = len(string)

    for i in range(length):
        bracket = string[i]
        if bracket in ["(", "[", "{"]:
            open_indexes[bracket].append(i)
        else:
            opposite = ["(", "[", "{"][[")", "]", "}"].index(bracket)]
            opposite_indexes = open_indexes[opposite]
            if opposite_indexes == []:
                return False
            distance = i - opposite_indexes[-1] - 1
            if distance == 0:
                opposite_indexes.pop()
            elif distance % 2 == 1:
                return False
            else:
                for other_bracket, indexes in open_indexes.items():
                    if other_bracket != bracket and indexes != []:
                        if opposite_indexes[-1] < indexes[-1] < i:
                            return False
                opposite_indexes.pop()

    for indexes in open_indexes.values():
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
