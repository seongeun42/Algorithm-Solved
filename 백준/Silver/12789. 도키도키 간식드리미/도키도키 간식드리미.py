import sys
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())][::-1]
waiting = []
cur = 1
while nums or waiting:
    if waiting and cur == waiting[-1]:
        waiting.pop()
        cur += 1
        continue
    if nums:
        f = nums.pop()
        if cur == f:
            cur += 1
        elif cur < f and (not waiting or waiting[-1] > f):
            waiting.append(f)
        else:
            print("Sad")
            break
else:
    print("Nice")