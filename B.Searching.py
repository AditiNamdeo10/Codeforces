N=int(input())
lst=list(map(int,input().split()))
X=int(input())
if X in lst:
    print(lst.index(X))
else:
    print("-1")