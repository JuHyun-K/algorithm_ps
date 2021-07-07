'''
인공지능 시계
'''

h, m, s = map(int, input().split())
start = int(input())

time = h*60*60 + m*60 + s + start
h = time//60//60%24
m = time//60%60
s = time%60
print(h,m,s)

