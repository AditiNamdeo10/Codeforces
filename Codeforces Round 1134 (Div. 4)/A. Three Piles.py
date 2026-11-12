t=int(input())

for _ in range(t):
    d1, d2=0,0
    a,b,c=map(int,input().split())
    d1=b-a
    d2=c-b
    if(d1==1 and d2==1):
        print("YES")
    else:
        print("NO")

