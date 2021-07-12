from sys import stdin

t = int(stdin.readline())

for i in range(t):
    k_score, y_score = 0, 0
    for j in range(9):
        y, k = map(int, stdin.readline().split())
        k_score += k
        y_score += y
    if k_score > y_score:
        print("Korea")
    elif k_score < y_score:
        print("Yonsei")
    else:
        print("Draw")
