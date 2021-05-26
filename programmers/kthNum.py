# sort와 sorted의 차이: sort는 원본을 정렬, sorted는 원본은 건들ㄴ 정렬값을 return
def solve(array, commands):
    ans = []
    for i, j, k in commands:
        ans.append(sorted(array[i-1:j])[k-1])
    return ans


def solution(array, commands):
    answer = solve(array, commands)
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
