N = int(input())
S = input()
if N % 2 == 1:
    print(-1)
else:
    stack = []
    ans = 0
    for c in S:
        if c == '(':
            if len(stack) == 0 or stack[-1] == '(':
                stack.append('(')
            else:
                cnt = len(stack)
                stack.pop()
                if ans < cnt:
                    ans = cnt
        else:
            if len(stack) == 0 or stack[-1] == ')':
                stack.append(')')
            else:
                cnt = len(stack)
                stack.pop()
                if ans < cnt:
                    ans = cnt
    print(ans if len(stack) == 0 else -1)