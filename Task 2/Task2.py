def dnaSequence(arr):
    fin=""
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i][-1]==arr[j][0]:
                fin+=arr[i]
                fin+=arr[j]

    return fin







inputs = []
while True:
    inp = input()
    if inp == "":
        break
    inputs.append(inp)

print(dnaSequence(inputs))