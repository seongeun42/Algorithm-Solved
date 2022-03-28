X = [*map(int, list(input()))]
cnt = 0
while len(X) != 1:
    X = [*map(int, list(str(sum(X))))]
    cnt += 1
print(cnt)
print("NO" if X[0] % 3 else "YES")