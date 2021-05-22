'''
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
완주하지 못한 사람은 1명임!
'''
def solve(part, comp):
    #각각 뒤집어서 정렬 -> 마지막것을 비교하는 식으로
    part.sort(reverse=True)
    comp.sort(reverse=True)
    name = ''
    for i in range(len(comp)-1, -1, -1):
        if(comp[-1] == part[-1]): #마지막 것이 서로 같으면 삭제
            del part[-1]
            del comp[-1]
        else: #마지막것이 서로 다르면, 완주하지 못한 경우(참가자 목록에 존재)
            name = part[-1]
            break
        
    if(name == ''):
        name = part[0]
    return name


def solution(participant, completion):
    answer = solve(participant, completion)
    return answer

li = ["mislav", "stanko", "mislav", "ana"]
li2 = ["stanko", "ana", "mislav"]

#li = ["marina", "josipa", "nikola", "vinko", "filipa"]
#li2 = ["josipa", "filipa", "marina", "nikola"]
print(solution(li, li2))
