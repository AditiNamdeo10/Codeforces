N=int(input())
lst=list(map(int,input().split()))

for i in range(len(lst)):
    if lst[i]==0:
        pass        
    elif lst[i]>0:
        lst[i]=1
    else:
        lst[i]=2
    print(lst[i],end=" ")
        