N=int(input())
A=list(map(int,input().split()))

ans=float('inf')

for i in A:
    c=0
    while(i%2==0):
        c+=1
        i=i//2
    ans=min(ans,c)
print(ans)