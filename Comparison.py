c=input()
A, s, B= c.split()
# c[0], c[2], c[4]
A=int(A)
B=int(B)
if s=='<' and A<B:
    print("Right")
elif s=='>' and A>B:
    print("Right")
elif s=="=" and A==B:
    print("Right")
else:
    print("Wrong")