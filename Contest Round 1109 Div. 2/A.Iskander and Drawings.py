t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    s=input()
    maxsub=0
    curr=0
    for i in s:
        if i=="#":
            curr+=1
            if curr>maxsub:
                maxsub=curr
        else:
                curr=0
    ans.append((maxsub+1)//2)
for ele in ans:
    print(ele)
    # c=0
    # for i in range(len(s)-1):
    #     if(s[i]=='#' and s[i]==s[i+1]):
    #         c=c+1
    # if c==0 or c==1 :
    #     ans.append(c)
    # elif c==2:
    #     ans.append(c-1)
    # elif (c+1)%2==0:
    #     ans.append((c+1)//2)
    # else:
    #     ans.append(((c+1)//2)+1)
# for ele in ans:
#    print(ele)