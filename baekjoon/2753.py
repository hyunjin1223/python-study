# problem: 2753
# tier: bronze

# 연도 입력
year = int(input())

# 윤년 조건 판별 (4의 배수이면서 100의 배수가 아님, 또는 400의 배수)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1)
else:
    print(0)