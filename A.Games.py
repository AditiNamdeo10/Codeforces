n=int(input())

h=[]
a=[]
ans=0

for _ in range(n):
    x, y=map(int,input().split())
    h.append(x)
    a.append(y)

for i in range(n):
    for j in range(n):
        if(i!=j and h[i]==a[j]):
            ans+=1

print(ans)