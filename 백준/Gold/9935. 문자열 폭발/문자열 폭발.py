s1 = list(input()[::-1])
s2 = [('', 0)]
target = input()
while s1:
    if s1[-1] == target[s2[-1][1]]:
        s2.append((s1.pop(), s2[-1][1] + 1))
        if s2[-1][1] == len(target):
            for _ in range(len(target)):
                s2.pop()
    else:
        if s1[-1] == target[0]:
            s2.append((s1.pop(), 1))
        else:
            s2.append((s1.pop(), 0))
ans = list(zip(*s2))[0]
print("".join(ans) if len(ans) > 1 else "FRULA")