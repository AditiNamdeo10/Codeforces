n=int(input())
s=input()
ca=s.count('A')
cd=s.count('D')
if ca>cd:
    print("Anton")
elif ca<cd:
    print("Danik")
else:
    print("Friendship")