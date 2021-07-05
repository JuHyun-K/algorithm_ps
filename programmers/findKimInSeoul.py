def solution(seoul):
    answer = ''
    if("Kim" in seoul):
        idx = seoul.index("Kim")
    answer = "김서방은 "+str(idx)+"에 있다"
    return answer



seoul = ["Jane", "Kim"]
print(solution(seoul))
