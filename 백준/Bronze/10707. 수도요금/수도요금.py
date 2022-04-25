I = [int(input()) for _ in range(5)]
X = I[0] * I[-1]
Y = I[1] if I[-1] <= I[2] else I[1] + I[3] * (I[-1] - I[2])
print(min(X, Y))