def is_continuous_chk(nums):
    if len(nums) < 5:
        return False
    tmp = sorted(list(nums))
    for i in range(1, 5):
        if tmp[i] - tmp[i - 1] != 1:
            return False
    return True

def numbers(num):
    max_num = 0
    four, three = 0, 0
    two = []
    for i in range(1, 10):
        if num[i] == 4:
            four = i
        elif num[i] == 3:
            three = i
        elif num[i] == 2:
            two.append(i)
        if num[i] > 0:
            max_num = i
    return max_num, four, three, two

def solve():
    card = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
    num = [0] * 10
    nums = set()
    for _ in range(5):
        c, n = input().split()
        n = int(n)
        card[c] += 1
        num[n] += 1
        nums.add(n)
    is_continuous = is_continuous_chk(nums)
    max_num, four, three, two = numbers(num)
    if 5 in card.values() and is_continuous:
        print(max_num + 900)
    elif four > 0:
        print(four + 800)
    elif three > 0 and len(two) > 0:
        print(three * 10 + two[0] + 700)
    elif 5 in card.values():
        print(max_num + 600)
    elif is_continuous:
        print(max_num + 500)
    elif three > 0:
        print(three + 400)
    elif len(two) == 2:
        print(two[1] * 10 + two[0] + 300)
    elif len(two) == 1:
        print(two[0] + 200)
    else:
        print(max_num + 100)

solve()