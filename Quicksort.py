def quick(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    low=[l[ind] for ind in range(1,len(l)) if pivot>l[ind]]
    high=[l[ind] for ind in range(1,len(l)) if pivot<=l[ind]]
    return quick(low)+[pivot]+quick(high)
l=[29,3,19,-10,44,1]
print(quick(l))