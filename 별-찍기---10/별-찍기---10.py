def recurive(pre, n):
    cur = []
    if n == 3:
        return pre
    for i in pre:
        cur.append(i * 3)
    for i in pre:
        cur.append(i + ' ' * len(pre) + i)
    for i in pre:
        cur.append(i * 3)
    return recurive(cur, n // 3)

n = int(input())
three = ["***", "* *", "***"]
print('\n'.join(recurive(three, n)))