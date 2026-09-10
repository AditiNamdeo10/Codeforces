s=input()
res=''
for i in s:
    if  i.lower() in 'aeiouy':
        pass
    else:
        res+='.'
        if i.isupper():
            res+=i.lower()
        else:
            res+=i
print(res)
        