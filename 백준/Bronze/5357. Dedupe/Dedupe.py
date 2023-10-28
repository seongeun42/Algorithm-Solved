T = int(input())
for _ in range(T):
    s = input()
    ns = [s[0]]
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            ns.append(s[i])
    print("".join(ns))