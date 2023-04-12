import sys
while 1:
    s = sys.stdin.readline().rstrip()
    if s == ".": break
    stack = []
    chk = 0
    for c in s:
        if c in ["(", "["]:
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(": stack.pop()
            else: chk = 1
        elif c == "]":
            if stack and stack[-1] == "[": stack.pop()
            else: chk = 1
        if chk == 1: break
    print("no" if chk or stack else "yes")