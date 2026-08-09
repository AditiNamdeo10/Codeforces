n=int(input())
curr=0
caps=0

for i in range(n):
    exit,enter=map(int,input().split())
    curr-=exit
    curr+=enter

    caps=max(caps,curr)

print(caps)