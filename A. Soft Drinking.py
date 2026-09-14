n, k, l, c, d, p, nl, np=map(int,input().split())

a= k*l//nl   #mililiters of drink available
b= c*d       #Lime slice available
e= p//np     #grams of salt

print(min(a,b,e)//n)  #total toast/number of friends=toast per friend