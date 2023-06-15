"""
Solution of CS-centric task
"""
def dna_sequence(arr):
    """
    This function do the process of DNA sequence assembly.
    """
    final = arr[0]
    for i in range(1, len(arr)):
        match = find_match(final, arr[i])
        final += arr[i][match:]
    return final


def find_match(str1, str2):
    """
    This function find the match of two dna sequence.
    """
    max_len = min(len(str1), len(str2))
    for i in range(max_len, 0, -1):
        if str1[-i:] == str2[:i]:
            return i


inputs = []
while True:
    inp = input()
    print(inp)
    if inp == "":
        break
    inputs.append(inp)
print(inputs)
print(dna_sequence(inputs))
