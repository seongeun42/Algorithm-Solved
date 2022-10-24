s = [[i, int(input())] for i in range(1, 9)]
ans = list(zip(*sorted(s, key=lambda x: -x[1])[:5]))
print(sum(ans[1]))
print(*sorted(ans[0]), sep=" ")