s=input()
s=s.replace('{','').replace('}','').replace(',','').replace(' ','')
if s=="":
    print("0")
else:
    print(len(set(s)))