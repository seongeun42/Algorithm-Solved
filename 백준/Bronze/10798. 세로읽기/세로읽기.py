s = [input() for _ in range(5)]
for i in range(len(max(s, key=len))):
    for j in range(5):
        if i < len(s[j]):
            print(s[j][i], end='')