N=int(input())
A=list(map(int,input().split()))
minEle=min(A)
maxEle=max(A)

idx=A.index(minEle)
idx2=A.index(maxEle)


A[idx],A[idx2]=maxEle,minEle

for i in A:
    print(i,end=' ')