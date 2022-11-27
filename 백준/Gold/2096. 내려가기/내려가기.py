import sys
input = sys.stdin.readline

n = int(input())
max_dp = [*map(int, input().split())]
min_dp = max_dp
for _ in range(n - 1):
    new_line = [*map(int, input().split())]
    max_tmp = []
    min_tmp = []
    for col in range(3):
        col_min = 0 if col == 0 else col - 1
        col_max = 3 if col == 2 else col + 2
        max_tmp.append(new_line[col] + max(max_dp[col_min:col_max]))
        min_tmp.append(new_line[col] + min(min_dp[col_min:col_max]))
    max_dp = max_tmp
    min_dp = min_tmp
print(max(max_dp), min(min_dp))