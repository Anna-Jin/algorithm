# 2016년
def solution1(a, b):
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    monthDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    c = ((sum(monthDay[:a - 1]) + b) % 7) - 1

    answer = week[c]
    return answer

print(solution1(5, 24))
print("================================")

# 나누어 떨어지는 숫자 배열
def solution2(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)

    answer.sort()

    return answer

arr = [3,2,6]
divisor = 10
print(solution2(arr, divisor))
print("================================")