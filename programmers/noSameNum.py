def solution(arr):
    answer = []
    #순서유지
    #숫자가 연속적으로 나타나면 1개만 유지

    tmp = -1
    for ele in arr:
        if(tmp != ele):
             answer.append(ele)
        tmp = ele
    return answer



arr = [1,2,1]
print(solution(arr))
