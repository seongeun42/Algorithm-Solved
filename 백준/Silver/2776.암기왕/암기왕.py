t = int(input())
for _ in range(t):
    n = int(input())
    s1 = {v:1 for v in list(map(int, input().split()))}
    m = int(input())
    s2 = list(map(int, input().split()))
    for k in s2:
        print(1 if k in s1 else 0)