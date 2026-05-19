N =int(input())
sum=0
lst=list(map(int,input().split()))
for i in range(N):
    sum+=lst[i] 
print(abs(sum))
