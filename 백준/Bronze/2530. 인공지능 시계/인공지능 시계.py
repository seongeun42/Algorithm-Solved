A, B, C = map(int, input().split())
D = int(input())
dm, dd = divmod(D, 60)

if dd + C >= 60:
    B += dm + 1
    C += dd - 60
else:
    B += dm
    C += dd
    
if B >= 60:
    A += B // 60
    B %= 60

if A >= 24:
    A %= 24
    
print(A, B, C)