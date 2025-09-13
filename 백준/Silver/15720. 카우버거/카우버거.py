import sys
input = sys.stdin.readline

B, C, D = map(int, input().split())
burger = sorted([*map(int, input().split())], reverse=True)
side = sorted([*map(int, input().split())], reverse=True)
drink = sorted([*map(int, input().split())], reverse=True)
cnt = min(B, C, D)
before = sum(burger) + sum(side) + sum(drink)
after = before - sum(burger[:cnt]) * 0.1 - sum(side[:cnt]) * 0.1- sum(drink[:cnt]) * 0.1  
print(before)
print(int(after))