S = input()
T = list(input())
while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]
    if ''.join(T) == S:
        print(1)
        break
if not T:
    print(0)