N = int(input())
crains = sorted([*map(int, input().split())], reverse=True)
M = int(input())
boxes = sorted([*map(int, input().split())], reverse=True)
if crains[0] < boxes[0]:
    print(-1)
else:
    cnt = 0
    while boxes:
        cnt += 1
        for i in range(N):
            for j in range(len(boxes)):
                if boxes[j] <= crains[i]:
                    boxes.pop(j)
                    break
    print(cnt)