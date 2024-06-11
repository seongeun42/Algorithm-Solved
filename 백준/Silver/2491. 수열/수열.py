N = int(input())
arr = [*map(int, input().split())]
decr_ans = 1
incr_ans = 1
decr_tmp = 1
incr_tmp = 1
for i in range(1, N):
    if arr[i - 1] <= arr[i]:
        incr_tmp += 1
    if arr[i - 1] >= arr[i]:
        decr_tmp += 1
    if arr[i - 1] > arr[i] or i == N - 1:
        if incr_ans < incr_tmp:
            incr_ans = incr_tmp
        incr_tmp = 1
    if arr[i - 1] < arr[i] or i == N - 1:
        if decr_ans < decr_tmp:
            decr_ans = decr_tmp
        decr_tmp = 1
print(max(decr_ans, incr_ans))