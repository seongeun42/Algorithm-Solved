n = int(input())
paper = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1
print(sum(map(sum, paper)))