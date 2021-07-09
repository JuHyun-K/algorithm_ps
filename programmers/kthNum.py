# sort와 sorted의 차이: sort는 원본을 정렬, sorted는 원본은 건들ㄴ 정렬값을 return

def solution(array, commands):
    answer = []
    for ele in commands:
        answer.append(sorted(array[ele[0]-1:ele[1]])[ele[2]-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution2(array, commands))
