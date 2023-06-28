c = int(input())
for _ in range(c):
    s = [*map(int, input().split())][1:]
    avg = sum(s) / len(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] > avg:
            cnt += 1
    print(f"{cnt / len(s) * 100:.3f}%")