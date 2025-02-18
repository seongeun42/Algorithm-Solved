import sys
input = sys.stdin.readline

n = int(input())
town = [*map(int, input().split())]
print(sum(town) - max(town))