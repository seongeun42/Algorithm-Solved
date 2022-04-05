def cal(arr):
    ans = 0
    for i in range(len(arr) - 1):
        ans += abs(A[arr[i]] - A[arr[i + 1]])
    return ans

def dfs(dep):
    global res
    if dep == N:
        res = max(res, cal(arr))
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            arr.append(i)
            dfs(dep + 1)
            arr.pop()
            visit[i] = 0

N = int(input())
A = [*map(int, input().split())]
arr = []
visit = [0] * N
res = -1e9
dfs(0)
print(res)