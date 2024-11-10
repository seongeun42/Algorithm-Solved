score = {"K": 0, "P": 1, "N": 3, "B": 3, "R": 5, "Q": 9}
ans = 0
for _ in range(8):
    s = input()
    for c in s:
        if c == '.':
            continue
        if c.islower():
            ans -= score[c.upper()]
        else:
            ans += score[c]
print(ans)