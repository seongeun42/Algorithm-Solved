N, K = map(int, input().split())
nums = sorted([*map(int, input().split())], reverse=True)
print(sum(nums[:K]) - ((K - 1) * K // 2))