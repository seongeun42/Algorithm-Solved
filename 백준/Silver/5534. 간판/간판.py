import sys
input = sys.stdin.readline

def check(new, old):
    start = [i for i in range(len(old)) if old[i] == new[0]]
    for s in start:
        for t in range(1, len(old)):
            idx = 0
            for c in old[s::t]:
                if c == new[idx]:
                    idx += 1
                else:
                    idx = 0
                if idx == len(new):
                    return 1
    return 0

N = int(input())
new = input().rstrip()
ans = 0
for _ in range(N):
    old = input().rstrip()
    ans += check(new, old)
print(ans)