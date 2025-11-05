import sys
input = sys.stdin.readline

s = input()
problem = 0
while 1:
    s = input().rstrip()
    if s == "고무오리 디버깅 끝":
        break
    elif s == "문제":
        problem += 1
    elif s == "고무오리":
        if problem == 0:
            problem += 2
        else:
            problem -= 1
print("고무오리야 사랑해" if problem == 0 else "힝구")