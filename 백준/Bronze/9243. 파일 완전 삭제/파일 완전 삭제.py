N = int(input())
a, b = list(input()), list(input())
for _ in range(N):
    for i in range(len(a)):
        a[i] = '0' if a[i] == '1' else '1'
print(f"Deletion {'succeeded' if a == b else 'failed'}")