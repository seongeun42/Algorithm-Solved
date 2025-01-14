N = int(input())
S = input()
ans = 0
bonus = 0
for i in range(len(S)):
    if S[i] == 'O':
        ans += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0  
print(ans)