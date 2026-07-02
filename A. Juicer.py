n, b, d=map(int,input().split())
lst=list(map(int,input().split()))
totalsize=0
c=0
for i in lst:
    if i>b:
        continue
    totalsize+=i
    if totalsize>d:
        c+=1
        totalsize=0
print(c)