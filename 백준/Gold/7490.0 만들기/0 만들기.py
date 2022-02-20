def dfs(i, exp):
    if i == N:
        if eval(exp.replace(" ", "")) == 0:
            print(exp)
        return
    dfs(i + 1, exp + " " + str(i + 1))
    dfs(i + 1, exp + "+" + str(i + 1))
    dfs(i + 1, exp + "-" + str(i + 1))

T = int(input())
for _ in range(T):
    N = int(input())
    dfs(1, "1")
    print()