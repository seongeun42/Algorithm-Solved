def dfs(cur, pick, max_pick, s, pair, ans):
    if len(pick) == max_pick * 2:
        exp = []
        for i in range(len(s)):
            if i not in pick:
                exp.append(s[i])
        ans.add("".join(exp))
        return
    for i in range(cur + 1, len(pair)):
        pick.append(pair[i][0])
        pick.append(pair[i][1])
        dfs(i, pick, max_pick, s, pair, ans)
        pick.pop()
        pick.pop()

def solve():
    s = input()
    pair = []
    parentthese = []
    for i in range(len(s)):
        if s[i] == "(":
            parentthese.append(i)
        elif s[i] == ")":
            pair.append((parentthese.pop(), i))
    ans = set()
    for i in range(1, len(pair) + 1):
        dfs(-1, [], i, s, pair, ans)
    ans = sorted(list(ans))
    for e in ans:
        if e != s:
            print(e)

solve()