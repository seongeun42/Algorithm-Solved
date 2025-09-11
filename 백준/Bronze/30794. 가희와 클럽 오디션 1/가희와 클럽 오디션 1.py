arr = input().split()
if arr[1] == "miss":
    print(0)
elif arr[1] == "bad":
    print(200 * int(arr[0]))
elif arr[1] == "cool":
    print(400 * int(arr[0]))
elif arr[1] == "great":
    print(600 * int(arr[0]))
elif arr[1] == "perfect":
    print(1000 * int(arr[0]))