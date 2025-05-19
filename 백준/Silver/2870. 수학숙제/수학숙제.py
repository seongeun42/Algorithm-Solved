N = int(input())
ans = []
for _ in range(N):
    s = input().rstrip()
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i
            while i < len(s) and s[i].isdigit():
                i += 1
            ans.append(int(s[j:i]))
        else:
            i += 1
ans.sort()
print(*ans, sep="\n")