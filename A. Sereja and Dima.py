n=int(input())
lst=list(map(int,input().split()))
c1s=0
c2d=0
i=0
j=n-1
counter=1
while(i<=j):
    if(lst[i]>lst[j]):
        max=lst[i]
        i+=1
    else:
        max=lst[j]
        j-=1
    if(counter%2==1):
        c1s+=max
    else:
        c2d+=max
    counter+=1
print(c1s,c2d)
    
    