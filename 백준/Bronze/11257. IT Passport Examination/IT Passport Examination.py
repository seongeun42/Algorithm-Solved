n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    hap = b + c + d
    res = "FAIL" if hap < 55 or b / 35 < 0.3 or c / 25 < 0.3 or d / 40 < 0.3 else "PASS"
    print(f"{a} {hap} {res}")