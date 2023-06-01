def isPrime(num):
    if num in sosu:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    sosu.add(num)
    return True

def dfs(dep, num):
    if dep == N:
        print(num)
        return
    for i in range(10):
        tmp = num * 10 + i
        if isPrime(tmp):
            dfs(dep + 1, tmp)

N = int(input())
sosu = {2, 3, 5, 7}
for i in [2, 3, 5, 7]:
    dfs(1, i)