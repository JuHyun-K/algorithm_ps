from sys import stdin
x_arr = []
y_arr = []

for i in range(3):
    x, y = map(int, stdin.readline().split())
    x_arr.remove(x) if x in x_arr else x_arr.append(x)
    y_arr.remove(y) if y in y_arr else y_arr.append(y)

print(x_arr[0], y_arr[0])
print(*x_arr, *y_arr)