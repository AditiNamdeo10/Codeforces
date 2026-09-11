t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    lst.sort()

    possible = True

    for i in range(n - 1):
        if lst[i + 1] - lst[i] > 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")