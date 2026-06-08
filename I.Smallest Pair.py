T=int(input())
for _ in range(T):
  N=int(input())
  lst=list(map(int,input().split()))
  ans=float('inf')

  for i in range(N):
    for j in range(i+1,N):
        curr=lst[i]+lst[j]+(j-i)
        if curr<ans:
           ans=curr
  print(ans)


