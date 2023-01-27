# 2016년
def solution1(a, b):
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    monthDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    c = ((sum(monthDay[:a - 1]) + b) % 7) - 1

    answer = week[c]
    return answer

print(solution1(5, 24))



