arr = list(map(int, input().split()))
arr.sort()
'''
리스트로 정렬
set개수가 1개: 맨 앞
set이 3개: 맨뒤
set이 2개: 가운데 
'''
if len(set(arr)) == 1: #다 같은 수
    print(arr[0]*1000 + 10000)
elif len(set(arr)) == 3: #다 다른 수
    print(arr[2] * 100)
else:
    print(1000+arr[1]*100)