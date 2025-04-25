_ = int(input())
res = sum(map(int, input().split()))
if res == 0:
    print("Stay")
elif res < 0:
    print("Left")
else:
    print("Right")