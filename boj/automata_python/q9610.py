import sys

n = int(sys.stdin.readline())
points = [0, 0, 0, 0, 0]
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x*y == 0:
        points[4] += 1
    elif x*y > 0:
        if x > 0:
            points[0] += 1
        else:
            points[2] += 1
    else:
        if x < 0:
            points[1] += 1
        else:
            points[3] += 1

for i in range(5):
    if i < 4:
        print("Q"+str(i+1)+":", points[i])
    else:
        print("AXIS:", points[i])
