n, k=map(int,input().split())
for i in range(n):
    print(chr(ord('a')+(i%k)),end="")