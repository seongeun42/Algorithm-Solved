N = int(input())
topping = input().split()
cheese = set()
for s in topping:
    if s.endswith("Cheese"):
        cheese.add(s)
print("yummy" if len(cheese) >= 4 else "sad")