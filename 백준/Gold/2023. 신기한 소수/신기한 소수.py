def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def dfs(dep, num):
    if dep == N:
        print(num)
        return
    for i in range(1, 10, 2):
        tmp = num * 10 + i
        if isPrime(tmp):
            dfs(dep + 1, tmp)

N = int(input())
for i in [2, 3, 5, 7]:
    dfs(1, i)