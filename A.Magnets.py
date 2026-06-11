n=int(input())
lst=[]
for i in range(n):
    a=input()
    lst.append(a)
    c=1
for i in range(1,n):
    if lst[i][0]==lst[i-1][1]:
        c+=1
print(c)