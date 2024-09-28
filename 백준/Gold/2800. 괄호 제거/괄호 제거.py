def dfs(cur, pick, max_pick, s, pair, ans):
    if len(pick) == max_pick:
        exp = list(s)
        for l, r in pick:
            exp[l], exp[r] = '', ''
        ans.add("".join(exp))
        return
    for i in range(cur + 1, len(pair)):
        pick.append(pair[i])
        dfs(i, pick, max_pick, s, pair, ans)
        pick.pop()

def solve():
    s = input()
    pair = []
    brackets = []
    for i in range(len(s)):
        if s[i] == "(":
            brackets.append(i)
        elif s[i] == ")":
            pair.append((brackets.pop(), i))
    ans = set()
    for i in range(1, len(pair) + 1):
        dfs(-1, [], i, s, pair, ans)
    ans = sorted(list(ans))
    for e in ans:
        if e != s:
            print(e)

solve()