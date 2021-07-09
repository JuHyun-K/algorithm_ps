grade = input()
grades = [4, 3, 2, 1]

if grade == 'F':
    print(0.0)
elif grade[1] == '+':
    print(grades[ord(grade[0]) - 65]+0.3)
elif grade[1] == '-':
    print(grades[ord(grade[0]) - 65] - 0.3)
else:
    print(grades[ord(grade[0]) - 65]+0.0)
