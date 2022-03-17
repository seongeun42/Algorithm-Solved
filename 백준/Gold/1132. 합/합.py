N = int(input())
arr = [[0, 0] for _ in range(10)]
for _ in range(N):
    s = input()
    m = 1
    arr[ord(s[0]) - 65][1] = 1
    for c in s[::-1]:
        arr[ord(c) - 65][0] += m
        m *= 10
arr.sort(key=lambda x: -x[0])
if arr[9][1]:
    for i in range(8, -1, -1):
        if arr[i][1] == 0:
            del arr[i]
            break
res = 0
for i, v in enumerate(arr):
    res += v[0] * (9 - i)
print(res)