import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        button = [0] * 5
        sixty = N // 60
        ten = (N % 60) // 10
        one = N % 10
        if one > 5:
            ten += 1
            one -= 10
        if ten > 3:
            sixty += 1
            ten -= 6
        if ten < 0 and one == 5:
            ten += 1
            one -= 10
        button[0] = sixty
        button[2-(ten >= 0)] = abs(ten)
        button[4-(one >= 0)] = abs(one)
        print(*button)

solve()