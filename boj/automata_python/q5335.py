import sys

t = int(sys.stdin.readline())

for i in range(t):
    exp = sys.stdin.readline().rstrip().split()
    exp[0] = float(exp[0])
    for j in range(1, len(exp)):
        if exp[j] == '@':
            exp[0] *= 3
        elif exp[j] == '%':
            exp[0] += 5
        else:
            exp[0] -= 7
    print('%0.2f' % exp[0])
