J = [*map(int, input().split())]
S = [*map(int, input().split())]
ans = False
for i in range(1, 10):
    if sum(J[:i]) > sum(S[:i - 1]):
        ans = True
        break
print("Yes" if ans else "No")