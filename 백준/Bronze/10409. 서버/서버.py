n, T = map(int, input().split())
time = [*map(int, input().split())][::-1]
ans = 0
while time and T - time[-1] >= 0:
    ans += 1
    T -= time.pop()
print(ans)