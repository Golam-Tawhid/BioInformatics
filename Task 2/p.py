lst=['ATGAG','AGGAA','AATTT']
for i in range(len(lst)):
    print(lst[i])
    for j in range(len(lst)):
        print(lst[j])
        for k in reversed(range(len(lst[i]))):
            print(lst[i][k])
            print((""))
            for m in range(len(lst[j])):
                print(lst[j][m])