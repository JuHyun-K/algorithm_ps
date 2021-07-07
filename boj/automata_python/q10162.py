'''
전자레인지
가장 작은 단위를 봄(10초미만이면 -1이라는 것을 미리 파악!)
'''
five, one, ten = 0, 0, 0

t = int(input())

while t > 9:
    if t//300 > 0:
        five += (t//300)
        t %= 300
    elif t//60 > 0:
        one += (t//60)
        t %= 60
    elif t//10 > 0:
        ten += (t//10)
        t %= 10

if t == 0:
    print(five, one, ten)
else:
    print(-1)

'''
T = int(input())
if T % 10: //while문 돌릴필요 없이..ㅋ
    print(-1)
else:
    print(T // 300, (T % 300) // 60, (T % 60) // 10)
'''