def backtrack(dep, total):
    global cnt
    if dep == N:
        return
    if total + nums[dep] == S:
        cnt += 1
    backtrack(dep + 1, total)
    backtrack(dep + 1, total + nums[dep])

N, S = map(int, input().split())
nums = sorted([*map(int, input().split())])
cnt = 0
backtrack(0, 0)
print(cnt)