# problem: 1629
# tier: silver
import sys

# 곱셈 문제

# 분할 정복을 이용한 거듭제곱
def power(a, b, c):
    # 지수가 1이면 나머지 반환
    if b == 1:
        return a % c

    # 지수를 절반으로 나누어 계산
    temp = power(a, b // 2, c)

    # 짝수 지수
    if b % 2 == 0:
        return (temp * temp) % c

    # 홀수 지수
    return (temp * temp * a) % c


a, b, c = map(int, sys.stdin.readline().split())

# A^B % C 출력
print(power(a, b, c))