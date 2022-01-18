# https://www.acmicpc.net/problem/11497

def get_difficulty(height_array, n):
    height_array.sort()

    result = 0
    for j in range(2, n):
        result = max(result, height_array[j]-height_array[j-2])
    
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    height_array = list(map(int, input().split()))
    print(get_difficulty(height_array, n))