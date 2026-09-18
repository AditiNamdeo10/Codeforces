t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    a = sorted(s)
    ans = 0

    for i in range(n):
        if s[i] != a[i]:
            ans += 1

    print(ans)