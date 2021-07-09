def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    return days[(sum(month[:a-1]) + b) % 7 - 1]



'''
1월1일은 금요일
월-1 + 일 -> 일수로 다 바꾸고
%7
'''
a, b = 12, 31
print(solution(a, b))
