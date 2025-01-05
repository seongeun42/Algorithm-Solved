X = input()
if X[0] == '0':
    print(int(X, 16) if X[1] == 'x' else int(X, 8))
else:
    print(X)