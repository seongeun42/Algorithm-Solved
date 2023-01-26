t = int(input())
for _ in range(t):
    s = input().split()
    ans = float(s[0])
    for i in range(1, len(s)):
        if s[i] == "@":
            ans *= 3
        elif s[i] == "%":
            ans += 5
        else:
            ans -= 7
    print(f"{ans:.2f}")