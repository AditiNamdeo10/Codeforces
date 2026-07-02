n, x=map(int,input().split())
dis=0
ice=x
for i in range(n):
    d=list(input().split())
    curr=int(d[1])
    if d[0]=='+':
        ice+=curr
    else:
        if(ice<curr):
            dis+=1
        else:
            ice-=curr
print(ice,dis,sep=' ')
        
    
