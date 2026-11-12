t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    c=0
    if s[0]=='B':
        c+=1

    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            c+=1
    print(c)
