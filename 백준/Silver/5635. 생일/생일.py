n = int(input())
c = [input().split() for _ in range(n)]
c.sort(key=lambda x : (int(x[3]), int(x[2]), int(x[1])))
print(c[-1][0])
print(c[0][0])
