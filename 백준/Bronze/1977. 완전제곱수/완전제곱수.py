m = int(input())
n = int(input())
ans = [i for i in range(m, n + 1) if i ** 0.5 == int(i ** 0.5)]
if ans:
    print(sum(ans), ans[0], sep="\n")
else:
    print(-1)