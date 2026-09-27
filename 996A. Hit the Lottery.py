n=int(input())
c=0
# while(n>0):
#     if n>=100:
#         c+=1
#         n-=100
#     elif n>=20:
#         c+=1
#         n-=20
#     elif n>=10:
#         c+=1
#         n-=10
#     elif n>=5:
#         c+=1
#         n-=5
#     else:
#         c+=n 
#         break
# print(c)

c+=n//100
n%=100

c+=n//20
n%=20


c+=n//10
n%=10

c+=n//5
n%=5

c+=n
print(c)