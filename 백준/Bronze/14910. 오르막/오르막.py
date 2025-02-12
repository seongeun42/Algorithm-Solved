N = [*map(int,input().split())]
A = sorted(N)
print("Good" if N == A else "Bad")