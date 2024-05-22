n=int(input())
space=n//2
star=1
num=1
for l in range(n//2+1):
    print(' '*space+str(num)*star)
    space-=1
    star+=2
    num+=1
space=1
star=n-2
for l in range(n//2):
    print(' '*space+str(num)*star)
    space+=1
    star-=2
    num+=1