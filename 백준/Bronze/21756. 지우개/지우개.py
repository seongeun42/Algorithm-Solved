N = int(input())
ans = [i for i in range(1, N + 1)]
s = []
while len(ans) > 1:
    s = ans[::-1]
    ans = []
    i = 0
    while s:
        v = s.pop()
        if i % 2 == 1:
            ans.append(v)
        i += 1
print(ans[0])