import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        name, amount = sys.stdin.readline().split()
        dic[int(amount)] = name
    est = max(dic.keys())
    print(dic[est])
