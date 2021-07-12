import sys

while True:
    m, f = map(int, sys.stdin.readline().split())
    if (m,f) == (0,0):
        print("h")
        break
    if m+f == 0:
        break
    print(m+f)