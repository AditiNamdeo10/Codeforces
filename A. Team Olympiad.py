n=int(input())
p=[]
m=[]
e=[]
lst=list(map(int,input().split()))
for i in range(n):
    if lst[i]==1:
        p.append(i+1)
    elif lst[i]==2:
        m.append(i+1)
    else:
        e.append(i+1)
w=min(len(p),len(m),len(e))
print(w)

for i in range(w):
    print(p[i],m[i],e[i])