N=int(input())
prev=0
curr=1
for i in range(N-1):
    temp=prev
    prev=curr
    curr=temp+prev
print(prev)