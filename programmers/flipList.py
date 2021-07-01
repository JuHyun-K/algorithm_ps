def solution(n):
    answer = []
    #리스트(Str) -> 뒤집 -> 다시 int
    answer = list(str(n))
    answer.reverse()
    answer = list(map(int, answer))
    return answer

n = 12345
print(solution(n))
