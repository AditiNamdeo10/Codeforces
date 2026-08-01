t=int(input())
ans=[]
for _ in range(t):
    n, q= map(int,input().split())
    s=input().strip()
    for i in range(q):
        l, r, k=map(int,(input().split()))
        c0=0
        c1=0
        for j in range(l-1,r):
            if (j-(l-1))%2==0 :
                if s[j]!='0':
                   c0+=1
                if s[j]!='1':
                   c1+=1
            else:
                if s[j]!='1':
                   c0+=1
                if s[j]!='0':
                   c1+=1     
        if min(c0,c1)<=k:
            ans.append("YES")
        else:
            ans.append("NO")
for ele in ans:
    print(ele)


