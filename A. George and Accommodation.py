n=int(input())
cnt=0
for i in range(0,n):
    p, q= map(int,input().split())
    if q-p >=2:
        cnt+=1
print(cnt)

