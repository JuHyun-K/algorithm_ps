def solution(strings, n):
    strings.sort()
    answer = []
    dic = {}
    sortedList = []
    #strings의 각 원소에서 n번째 문자를 가져와서 딕셔너리 리스트 생성(ordered)
        # 키는 idx, value는 문자(char)
    #ordered의 value값으로 정렬
        #같은 char값은 각 리스트의 값을 가져와서 비교해서 정렬 -> 처음부터  정렬
        
    for i in range(len(strings)):
         dic[i] = strings[i][n]

    sortedList = sorted(dic.items(), key=lambda x: x[1])

    for i in range(len(sortedList)):
        idx = sortedList[i][0]
        answer.append(strings[idx])

    return answer


strings = ["abce", "abcd", "cdx"]
n = 1
print(solution(strings, n))
