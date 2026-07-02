n, t, k, d=map(int,input().split())

one_time=((n+k-1)//k)*t
cakes=0

for time in range(1,one_time):
    if time%t==0:
        cakes+=k
    if time>=(d+t) and (time-d)%t==0:
        cakes+=k

    if cakes>=n:
        print("YES")
        break
else:
    print("NO")