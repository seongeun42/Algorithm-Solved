n = int(input())
num = map(int, input().split())
m = len([i for i in num if i % 2 == 0])
print("Happy" if m > n - m else "Sad")