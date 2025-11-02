import sys
input = sys.stdin.readline

N = int(input())
ans = []
answer = [((i - 1) % 5) + 1 for i in range(1, 11)]
for i in range(N):
    arr = [*map(int, input().split())]
    cor = sum([1 for j in range(10) if arr[j] == answer[j]])
    if cor == 10:
        ans.append(i + 1)
print(*ans, sep='\n')