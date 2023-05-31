N, A, B = map(int, input().split())
if N <= B and A == B:
    print("Anything")
elif N <= B and A > B:
    print("Subway")
else:
    print("Bus")