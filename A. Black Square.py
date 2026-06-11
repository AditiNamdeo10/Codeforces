lst=list(map(int,input().split()))
s=input()
c=0
for i in s:
    i1=int(i)
    c+=lst[i1-1]
print(c)
