s=list(map(int,input().split('+')))
s.sort()
temp=''
for i in s:
   temp+=(str(i)+'+')
print(temp.rstrip('+'))