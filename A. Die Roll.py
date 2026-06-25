
y, w = map(int, input().split())

num = 7 - max(y, w)

if num % 6 == 0:
    print(f"{num//6}/1")
elif num % 3 == 0:
    print(f"{num//3}/2")
elif num % 2 == 0:
    print(f"{num//2}/3")
else:
    print(f"{num}/6")