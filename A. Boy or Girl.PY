S=input()
lst=[]
c=0
for i in S:
   if i in lst:
      continue
   else:
      c+=1
      lst.append(i)

if (c%2)==1:
   print("IGNORE HIM!")
else:
   print("CHAT WITH HER!")