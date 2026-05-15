N, A, B=map(int,input().split())
sum=0
for i in range(N+1):
    c=0
    s=str(i)
    for j in s:
        c+=int(j)
    if c>=A and c<=B:
        sum+=i
print(sum)