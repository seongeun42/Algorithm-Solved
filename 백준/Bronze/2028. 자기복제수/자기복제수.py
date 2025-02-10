N = int(input())

for _ in range(N):
    num = int(input())
    k = len(str(num))
    print("YES" if str(num ** 2)[-k:] == str(num) else "NO")