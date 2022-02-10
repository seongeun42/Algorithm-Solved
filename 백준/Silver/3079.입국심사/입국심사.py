import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])
s, e = T[0], T[-1] * M
res = 0
while s <= e:
    mid = (s + e) // 2
    
    people = 0
    for t in T:
        people += mid // t
        
    if people >= M:
        e = mid - 1
        res = mid
    else:
        s = mid + 1
print(res)