# problem: 1735
# tier: silver
import sys

# 유클리드 호제법을 이용한 최대공약수(GCD) 계산 함수
def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 분수 1: a/b, 분수 2: c/d 입력
a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

# 1. 두 분수를 더함
# 합의 분자 = (a * d) + (c * b)
# 합의 분모 = b * d
numerator = a * d + c * b
denominator = b * d

# 2. 기약분수로 만들기 위해 분자와 분모의 최대공약수를 구함
common = get_gcd(numerator, denominator)

# 3. 분자와 분모를 최대공약수로 나누어 출력
# (numerator // common) (denominator // common) 순서
print(numerator // common, denominator // common)