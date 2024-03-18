import sys
input = sys.stdin.readline

def make_hap(start, end, idx):
    if start == end:
        hap[idx] = nums[start - 1]
        return hap[idx]
    mid = (start + end) // 2
    hap[idx] = make_hap(start, mid, idx * 2) + make_hap(mid + 1, end, idx * 2 + 1)
    return hap[idx]

def sum(start, end, idx, left, right):
    # 범위 밖
    if right < start or left > end:
        return 0
    # 둘 다 범위 안
    if left <= start and end <= right:
        return hap[idx]
    # 한쪽만 범위 안
    mid = (start + end) // 2
    return sum(start, mid, idx * 2, left, right) + sum(mid + 1, end, idx * 2 + 1, left, right)

def update_num(start, end, idx, target, diff):
    # 범위 밖
    if target < start or end < target:
        return
    # 범위 내
    hap[idx] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update_num(start, mid, idx * 2, target, diff)
    update_num(mid + 1, end, idx * 2 + 1, target, diff)

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
# 구간 합 트리 구하기
hap = [0] * (N * 4)
make_hap(1, N, 1)

# 값 수정 및 구간 합 구하기
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - nums[b - 1]
        nums[b - 1] = c
        update_num(1, N, 1, b, diff)
    elif a == 2:
        print(sum(1, N, 1, b, c))