n=int(input())
lst=list(map(int,input().split()))
police=0
c=0
for i in lst:
    if i>0:
        police+=i
    else:
        if police<=0:
            c+=1
        else:
            police-=1

print(c)
    
