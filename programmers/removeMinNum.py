def solution(arr):
    arr.remove(min(arr)) #제일 작은수 제거
    if(len(arr) == 0): #빈 리스트 처
        return [-1]
    return arr


arr = [10]
print(solution(arr))
