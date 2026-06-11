s=input()
upsum=0
lowsum=0
for i in s:
    if i.isupper():
        upsum+=1
    else:
        lowsum+=1
if lowsum>=upsum:
    print(s.lower())
else:
    print(s.upper())