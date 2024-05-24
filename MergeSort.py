def conquer(Mlist,Llist,Rlist):
    ind,lind,rind=0,0,0
    while lind<len(Llist) and rind<len(Rlist):
        if Llist[lind]>Rlist[rind]:
            Mlist[ind]=Rlist[rind]
            rind+=1
        else:
            Mlist[ind]=Llist[lind]
            lind+=1
        ind+=1
    while lind<len(Llist):
        Mlist[ind]=Llist[lind]
        lind+=1
        ind+=1
    while rind<len(Rlist):
        Mlist[ind]=Rlist[rind]
        ind+=1
        rind+=1
def Divide(L):
    if len(L)>1:
        left,right=L[:len(L)//2],L[len(L)//2:]
        Divide(left)
        Divide(right)
        conquer(L,left,right)
L=[55,11,44,99,55,0]
Divide(L)
print(L)