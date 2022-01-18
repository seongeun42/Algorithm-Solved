import sys

def solution():
    cities = int(sys.stdin.readline())
    asset = list(map(int,sys.stdin.readline().split()))
    total = int(sys.stdin.readline())
    start = 0
    end = total
    answer=0
    
    if sum(asset)<=total:
        return max(asset)

    while(start<=end):
        mid = (start+end) //2
        money=0

        for i in asset:
            if i>mid:
                money+=mid
            else:
                money+= i

        if money<=total:
            answer = max(answer,mid)
            start = mid + 1
        else:
            end = mid - 1

    return answer

print(solution())