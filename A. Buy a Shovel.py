k, r=map(int,input().split())

for n in range(1,11):
    last=(n*k)%10
    if last==0 or last==r:
        print(n)
        break