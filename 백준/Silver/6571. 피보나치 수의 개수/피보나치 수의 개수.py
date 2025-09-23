import sys
input = sys.stdin.readline

fi = [1, 2, 3]

while fi[-1] <= 10 ** 100:
    fi.append(fi[-1] + fi[-2])

while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    cnt = 0
    for v in fi:
        if a <= v <= b:
            cnt += 1
        if b <= v:
            break
    print(cnt)