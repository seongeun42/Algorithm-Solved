import sys
input = sys.stdin.readline

def first(score):
    if score == 0: return 0
    elif score == 1: return 500
    elif score <= 3: return 300
    elif score <= 6: return 200
    elif score <= 10: return 50
    elif score <= 15: return 30
    elif score <= 21: return 10
    else: return 0
    
def second(score):
    if score == 0: return 0
    elif score == 1: return 512
    elif score <= 3: return 256
    elif score <= 7: return 128
    elif score <= 15: return 64
    elif score <= 31: return 32
    else: return 0

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print((first(a) + second(b)) * 10000)
        