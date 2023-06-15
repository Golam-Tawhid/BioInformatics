"""
This function returns the final sequence
"""


def dna_sequence(arr):
    """
    Find the matches and add them together
    """
    fin = ""

    for i, dna1 in enumerate(arr):
        for j, dna2 in enumerate(arr):
            idx = -1
            while idx >= -5:
                prefix = dna1[idx:]
                idx -= 1
                if dna2.startswith(prefix) and i != j:
                    fin += dna1
                    fin += dna2.lstrip(prefix)
                    break

    return fin


inpFile = open("Task 2/input2.txt", "r", encoding='utf-8')
outFile = open("Task 2/output2.txt", "w", encoding='utf-8')

inputs = []
while True:
    inp = inpFile.readline()
    print(inp)
    if inp == "":
        break
    inputs.append(inp)
print(inputs)
print(dna_sequence(inputs), file=outFile)
outFile.close()
