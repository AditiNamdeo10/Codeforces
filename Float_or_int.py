N=input()
parts=N.split('.')
a,b= parts[0],parts[1]

if int(b)==0:
    print(f"int {a}")
else:
    print(f"float {a} 0.{b}")
