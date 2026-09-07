n=int(input())
lst=[]
for _ in range(2):
    temp=list(map(int,input().split()))
    lst.extend(temp[1:])
lst=set(lst)
for i in range(1,n+1):
    if i not in lst:
        print("Oh, my keyboard!")
        break
else:
    print("I become the guy.")
    