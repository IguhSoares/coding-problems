"""Coding Problem #29
Run-length encoding and decoding

Example: 'AAAABBBCCDAA' <=> '4A3B2C1D2A'
"""
def encode(word: str) -> str:
    result: str = ""
    i = 0
    length = len(word)
    while i < length:
        previous_letter = word[i]
        count: int = 0
        while i < length and word[i] == previous_letter:
            # Counts the repeating character
            count += 1
            i += 1
        result += f"{count}{previous_letter}"
    print(result)


encode("aaabccccdeff")


def decode(word: str) -> str:
    i = 0
    result: str = ""
    length = len(word)
    while i < length:
        j = int(word[i])
        while j > 0:
            # Appends character to the result string j times:
            result += word[i + 1]
            j -= 1
        # The string to decode has the /^(\d[Aa-Zz])+$/ format,
        #   so i is incremented by 2, to get the next digit character
        i += 2
    print(result)


decode("4a3b2c1f4z")
