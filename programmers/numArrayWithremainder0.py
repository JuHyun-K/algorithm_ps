def solution(arr, divisor):
    answer = []
    answer = list(filter(lambda x: x%divisor==0,arr))
    answer.sort()
    return answer if len(answer)!=0 else [-1]  


arr = [3,2,6]
divisor = 10

print(solution(arr, divisor))
