n = int(input())
print(len([1 for num in range(n) if int(input()) % 2 == 1]))