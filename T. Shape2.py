N=int(input())
j=N-1
for i in range(1,N+1):
    print(" "*j,end="")
    j-=1
    print("*"*(i*2-1))