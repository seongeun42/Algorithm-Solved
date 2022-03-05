A, B = map(list, input().split())
minA, maxA, minB, maxB = '', '', '', ''
for i, v in enumerate(A):
    if v == '5' or v == '6':
        minA += '5'
        maxA += '6'
    else:
        minA += v
        maxA += v
for i, v in enumerate(B):
    if v == '5' or v == '6':
        minB += '5'
        maxB += '6'
    else:
        minB += v
        maxB += v
print(int(minA) + int(minB), int(maxA) + int(maxB))