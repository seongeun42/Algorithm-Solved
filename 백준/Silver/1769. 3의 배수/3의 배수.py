X = input()
cnt = 0
while len(X) != 1:
    X = str(sum(map(int, X)))
    cnt += 1
print(cnt)
print("YES" if X in '369' else "NO")