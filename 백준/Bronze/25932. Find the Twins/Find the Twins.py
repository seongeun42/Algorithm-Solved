if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        answer = 'none'
        nums=list(map(int, input().split()))
        if 17 in nums and 18 in nums:
            answer = 'both'
        elif 17 in nums :
            answer = 'zack'
        elif 18 in nums:
            answer = 'mack'
        print(*nums)
        print(answer)
        if _ != n-1:
            print()