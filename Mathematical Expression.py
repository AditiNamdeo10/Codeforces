a=input()
A, S, B, Q, C= a.split()
A=int(A)
B=int(B)
C=int(C)
if S=='+' and A+B==C:
    print("Yes")
elif S=='-' and A-B==C:
    print("Yes")
elif S=='*' and A*B==C:
    print("Yes")
else:
    if S=='+':
        print(A+B)
    elif S=='-':
        print(A-B)
    elif S=='*':
        print(A*B)