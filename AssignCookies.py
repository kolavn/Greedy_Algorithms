def AssignCookies(greed, size):
    n = len(greed)
    c = len(size)
    l = 0 #cookie traversal
    r = 0 #greed factor traversal
    greed = sorted(greed)
    size = sorted(size)

    while l<c:
        if (size[l]>=greed[r]):
            r = r+1
        l = l+1

    return r # this index r gives the number of cookies assigned, satisfied children = r 

greed = [1,5,3,3,4]
size = [4,2,1,2,1,3]
print("The no.of children received cookies is", AssignCookies(greed, size))


