import sys
input = sys.stdin.readline

N = int(input())
cnt = {}
for _ in range(N):
    word = input().rstrip()
    change = {}
    after = []
    for c in word:
        if c not in change:
            change[c] = chr(len(change) + ord('a'))
        after.append(change[c])
    after = ''.join(after)
    cnt[after] = cnt.get(after, 0) + 1
ans = 0
for key, val in cnt.items():
    if val == 1:
        continue
    ans += (val * (val - 1)) // 2
print(ans)