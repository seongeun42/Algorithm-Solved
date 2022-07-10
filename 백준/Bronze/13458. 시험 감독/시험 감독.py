N = int(input())
As = [*map(int, input().split())]
B, C = map(int, input().split())
ans = 0
for A in As:
    if A <= B:
        ans += 1
        continue
    v = (A - B) / C
    ans += int(v) + 2 if v != int(v) else int(v) + 1
print(ans)