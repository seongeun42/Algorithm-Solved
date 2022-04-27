X = int(input())
L = input()
i, m, f = 0, 0, 0
while i < len(L):
    if abs(m - f) == X:
        if L[i] == 'M':
            if abs(m + 1 - f) == X + 1:
                if i != len(L) - 1 and L[i + 1] == 'W':
                    f += 1
                    m += 1
                    i += 2
                else:
                    break
            else:
                m += 1
                i += 1
        else:
            if abs(m - f - 1) == X + 1:
                if i != len(L) - 1 and L[i + 1] == 'M':
                    f += 1
                    m += 1
                    i += 2
                else:
                    break
            else:
                f += 1
                i += 1
    elif abs(m - f) < X:
        if L[i] == 'M':
            m += 1
        else:
            f += 1
        i += 1
print(m + f)