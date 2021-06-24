  
#폰 번호~
def solution(phone_number):
    answer = list(phone_number)
    for i in range(0, len(phone_number)-4):
        answer[i] = '*'

    return ''.join(answer)


print(solution("01033334444"))
