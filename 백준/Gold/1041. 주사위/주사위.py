def solve():
    N = int(input())
    num = [*map(int, input().split())]
    if N == 1:
        print(sum(num) - max(num))
        return
    dice = dict(zip("ABCDEF", num))
    one = min(num)
    two = 50000000
    three = 50000000
    for c1 in "ABCDEF":
        for c2 in "ABCDEF":
            if c1 == c2: continue
            if (c1, c2) in {("A", "F"), ("F", "A"), ("B", "E"), ("E", "B"), ("C", "D"), ("D", "C")}:
                continue
            hap = dice[c1] + dice[c2]
            if hap < two:
                two = hap
    for s in {"ABC", "ABD", "ADE", "ACE", "BCF", "BDF", "CFE", "DEF"}:
        hap = dice[s[0]] + dice[s[1]] + dice[s[2]]
        if hap < three:
            three = hap
    ans = one * 4 * (N - 1) * (N - 2) + one * (N - 2) * (N - 2)
    ans += two * (N - 2) * 4 + two * (N - 1) * 4
    ans += three * 4
    print(ans)

solve()