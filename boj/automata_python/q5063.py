from sys import stdin

n = int(stdin.readline())
results = ["advertise", "do not advertise", "does not matter"]

for i in range(n):
    r, e, c = map(int, stdin.readline().split())
    tmp = r + c
    if tmp < e:
        print(results[0])
    elif tmp == e:
        print(results[2])
    else:
        print(results[1])
