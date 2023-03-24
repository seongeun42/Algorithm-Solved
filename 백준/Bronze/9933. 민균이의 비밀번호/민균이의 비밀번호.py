n = int(input())
pw = [input() for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(i, n):
        if pw[i] == pw[j][::-1]:
            ans = i
            break
    if ans != -1: break
print(len(pw[i]), pw[i][len(pw[i]) // 2])