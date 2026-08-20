n = int(input())
a = list(map(int, input().split()))

minimum = a[0]
maximum = a[0]
count = 0

for i in range(1, n):
    if a[i] > maximum:
        count += 1
        maximum = a[i]

    elif a[i] < minimum:
        count += 1
        minimum = a[i]

print(count)