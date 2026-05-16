T=int(int(input()))
for _ in range(T):
  N=int(input())
  c=0
  while(N>0):
    if N%2==1:
      c+=1
    N=N//2
  print((2**c)-1)

  