T = int(input())
N = int(input())
print(f"Padaeng_i {'Cry' if T - sum(map(int, input().split())) > 0 else 'Happy'}")