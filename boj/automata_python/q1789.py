"""
n개의 자연수 합이 s
n의 최대값?

s = n*(n+1)/2
s = 200
200*2 = n*(n-1)
400 = n*(n-1)
루트 씌운 수 부터
"""
s = int(input())
n = int(s**0.5)
summ = 0
print(n)
for i in range(n, 0, -1):
    print(n)
    summ += n
print(summ)