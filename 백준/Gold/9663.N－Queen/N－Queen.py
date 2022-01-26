def check(r):
    for i in range(r):
        if q[i] == q[r] or abs(q[r] - q[i]) == r - i:
            return False
    return True

def dfs(r):
    global res
    if r == n:
        res += 1
        return
    for i in range(n):
        q[r] = i
        if check(r):
            dfs(r + 1)

n = int(input())
q = [0] * n
res = 0
dfs(0)
print(res)