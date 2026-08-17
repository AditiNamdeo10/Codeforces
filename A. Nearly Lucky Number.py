s=input()
count=0
for i in range(len(s)):
    curr=s[i]
    if curr=='4' or curr=='7':
        count+=1
if count==4 or count==7:
    print("YES")
else:
    print("NO")