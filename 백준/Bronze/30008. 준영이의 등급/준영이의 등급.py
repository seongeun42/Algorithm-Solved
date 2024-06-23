N, K = map(int, input().split())
G = [*map(int, input().split())]
score = [96, 89, 77, 60, 40, 23, 11, 4, -1]
ans = []
for g in G:
    v = g * 100 // N
    for i in range(9):
        if score[i] < v:
            ans.append(9 - i)
            break
print(*ans)