n, k= map(int,input().split())
t= 240-k
c=0
for i in range(1,n+1):
    if t>= 5*i:
        t-=5*i
        c+=1
    else:
        break 
print(c)