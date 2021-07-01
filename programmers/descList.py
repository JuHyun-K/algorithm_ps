def solution(s):
    if(len(s) == 1):
        return s

    #아스키코드가 큰 것부터 정렬
    #정렬이기 때문에 sort()를 써야함. reverse가 아니

    tmp = list(map(ord, s))
    tmp.sort(reverse=True)
    tmp = list(map(chr, tmp))

    return ''.join(tmp)

s = "Zbcdefg" #gDCAB
print(solution(s))
