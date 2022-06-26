idx, score = 0, 0
for i in range(5):
    s = sum(map(int, input().split()))
    if score < s:
        idx = i + 1
        score = s
print(idx, score)