price, amount, money = map(int, input().split())

parent = price * amount - money
print(parent if parent >= 0 else 0)
