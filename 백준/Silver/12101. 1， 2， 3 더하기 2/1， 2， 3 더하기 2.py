cnt = 0

def backtrack(arr, rest, k):
    global cnt
    if rest == 0:
        cnt += 1
        if cnt == k:
            print('+'.join(map(str, arr)))
            exit()
        return
    for v in [1, 2, 3]:
        if v <= rest:
            arr.append(v)
            backtrack(arr, rest - v, k)
            arr.pop()

n, k = map(int, input().split())
arr = []
backtrack(arr, n, k)
if cnt < k:
    print(-1)