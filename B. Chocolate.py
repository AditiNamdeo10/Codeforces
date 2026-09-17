n=int(input())
lst=list(map(int,input().split()))
add=[]
for i in range(len(lst)):
    if lst[i]==1:
        add.append(i)
if len(add) == 0:
    print(0)
else: 
    ans=1
    for i in range(len(add)-1):
       ans*= add[i+1]-add[i]
    print(ans)