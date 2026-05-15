from math import log
A, B ,C ,D=map(int,input().split())
if B*log(A) > D*log(C):
    print("YES")
else:
    print("NO")