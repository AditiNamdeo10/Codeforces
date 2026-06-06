N=int(input())
A=list(map(int,input().split()))
minimum=A[0]
c=0
for ele in A:
    if minimum>ele:
        minimum=ele
        c=1
    elif ele==minimum:
        c+=1
if c%2==0:
    print("Unlucky")
else:
    print("Lucky")
