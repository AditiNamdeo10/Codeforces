n, k =map(int,input().split())
lst=list(map(int,input().split()))
kp=lst[k-1]
cnt=0
for ele in lst:
    if ele >= kp and ele>0 :
        cnt+=1
print(cnt)

