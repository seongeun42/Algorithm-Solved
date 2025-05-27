import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    days = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    for i in range(3, 13):
        days[i] += days[i - 1]
    flowers = []
    for _ in range(N):
        sm, sd, em, ed = map(int, input().split())
        flowers.append([days[sm] + sd, days[em] + ed])
    flowers.sort(key=lambda x: (x[0], -x[1]))
    if flowers[0][0] > 60:
        print(0)
        return
    start, end = days[3] + 1, days[12]
    ans = 1
    s, e = flowers[0]
    last = flowers[0]
    for i in range(1, N):
        if e > end:
            break
        if start <= e < end and e < flowers[i][0]:
            print(0)
            return
        if flowers[i][1] > e:
            if last[0] < flowers[i][0] <= e:
                if flowers[i][0] > 60:
                    ans += 1
                    flowers[i][0] = e
            elif flowers[i][0] <= last[0]:
                flowers[i][0] = last[0]
            last = flowers[i]
            e = flowers[i][1]
    print(0 if e <= end or s > 60 else ans)

solve()