N=int(input())
A=list(map(int,input().split()))
low=A[0]
pos=0
for i in range(1,len(A)):
    if A[i]<low:
        low=A[i]
        pos=i
print(low,pos+1,sep=" ")