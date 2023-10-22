import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    s = input().strip()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
arr = sorted(dic.items(), key=lambda x: (x[1], x[0]))
print(*arr[-1])