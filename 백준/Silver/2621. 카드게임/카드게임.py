def numbers(num):
    four, three = 0, 0
    two = []
    is_continuous = True
    max_num = 0
    total = 0
    for i in range(1, 10):
        if max_num == 0 and num[i] > 0:
            max_num = i
        if num[i] == 4:
            return False, i, i, 0, []
        elif num[i] == 3:
            three = i
            is_continuous = False
            total += 3
        elif num[i] == 2:
            two.append(i)
            is_continuous = False
            total += 2
        elif num[i] == 1:
            if is_continuous and (max_num != i and max_num != i - 1):
                is_continuous = False
            total += 1
        elif num[i] == 0:
            if max_num > 0:
                is_continuous = False
            continue
        max_num = i
        if total == 5:
            return is_continuous, max_num, four, three, two

def solve():
    card = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
    num = [0] * 10
    for _ in range(5):
        c, n = input().split()
        n = int(n)
        card[c] += 1
        num[n] += 1
    is_continuous, max_num, four, three, two = numbers(num)
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