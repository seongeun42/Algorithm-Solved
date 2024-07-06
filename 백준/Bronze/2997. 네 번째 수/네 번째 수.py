abc = sorted([*map(int, input().split())])
if abc[1] - abc[0] == abc[2] - abc[1]:
    print(abc[2] + (abc[1] - abc[0]))
elif abc[1] - abc[0] == 2 * (abc[2] - abc[1]):
    print(abc[0] + (abc[2] - abc[1]))
else:
    print(abc[1] + (abc[1] - abc[0]))