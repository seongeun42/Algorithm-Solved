br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())
d = abs(jr - dr) + abs(jc - dc)
bcross = min(abs(jr - br), abs(jc - bc))
b = bcross + max(abs(jr - br), abs(jc - bc)) - bcross
if d == b:
    print("tie")
elif d > b:
    print("bessie")
else:
    print("daisy")