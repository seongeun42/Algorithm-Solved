N = int(input())
t = sorted([*map(int, input().split())], reverse=True)
for i in range(N):
    t[i] += i + 2
print(max(t))