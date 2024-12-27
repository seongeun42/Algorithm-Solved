count = int(input())
for i in range(count):
    h, w = map(int, input().split())
    for j in range(h):
        a = input()
        b = w - 1
        while b >= 0:
            print(a[b], end="")
            b = b - 1
        print()