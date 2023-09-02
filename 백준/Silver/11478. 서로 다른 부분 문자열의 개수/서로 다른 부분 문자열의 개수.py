def solve():
    S = input()
    ans = set()
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            ans.add(S[i:j])
    print(len(ans))

solve()