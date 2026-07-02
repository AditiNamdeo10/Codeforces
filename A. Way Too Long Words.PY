n=int(input())
ans=[]
for i in range(n):
    temp=input()
    if len(temp)>10:
      s=temp[0]+str(len(temp)-2)+temp[-1]
      ans.append(s)
    else:
       ans.append(temp)

for i in ans:
    print(i)
