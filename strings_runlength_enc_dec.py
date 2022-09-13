# Coding Problem #29
# Run-length encoding and decoding
# Example: 'AAAABBBCCDAA' <-> '4A3B2C1D2A'
def encode(word):
    result = ""
    i = 0
    length = len(word)
    while i < length:
        previous_letter = word[i]
        count = 0
        while i < length and word[i] == previous_letter:
            count += 1
            i += 1
        result += f"{count}{previous_letter}"
    print(result)


encode("aaabccccdeff")


def decode(word):
    i = 0
    result = ""
    length = len(word)
    while i < length:
        j = int(word[i])
        while j > 0:
            result += word[i + 1]
            j -= 1
        i += 2
    print(result)


decode("4a3b2c1f4z")
