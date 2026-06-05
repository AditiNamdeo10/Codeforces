N=int(input())
A=list(map(int,input().split()))
flag=True
for i in range(N//2):
    if A[i]!=A[N-(i+1)]:
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")

