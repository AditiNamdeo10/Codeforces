A, B=map(int,input().split())
s=input()
flag="Yes"
for i in range(A+B+1):
    curr=s[i]
    if i==A:
        if curr!='-':
            flag="No"
    else:
        if not curr.isdigit():
            flag="No"
print(flag)

