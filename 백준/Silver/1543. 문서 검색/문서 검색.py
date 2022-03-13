S = input()
find = input()
F = len(find)
i = 0
cnt = 0
while i <= len(S) - F:
    if S[i:i + F] == find:
        cnt += 1
        i += F
    else:
        i += 1
print(cnt)