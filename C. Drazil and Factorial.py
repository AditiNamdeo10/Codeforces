n=int(input())
a=int(input())
ans=1
while(a>0):
    rem=a%10
    fact=1
    for i in range(2,rem+1):
        fact=fact*i
    
    ans=ans*fact
    a=a//10

print(ans)