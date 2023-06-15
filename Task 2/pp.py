lst=['ATGAG','AGGAA','AATTT']
fin=""
for i in range(len(lst)):
    for j in range(len(lst)):
        m=-1
        while m>=-5:
            a=lst[i][m:len(lst[i])]
            # print(a)
            m-=1
            if lst[j].startswith(a) and i!=j:
                fin+=lst[i]
                fin+=lst[j].lstrip(a)
                # print(lst[j])
                break
print(fin)