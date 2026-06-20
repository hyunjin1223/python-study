# problem: 13241
# tier: silver
import sys

# 두 정수 A와 B를 입력받음 (A, B는 최대 10^8로 큰 수이므로 파이썬의 정수형 활용)
# 파이썬은 자동으로 큰 수 연산(Arbitrary-precision arithmetic)을 지원함
a, b = map(int, sys.stdin.readline().split())

# 최대공약수(GCD)를 구하는 유클리드 호제법 함수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수(LCM) 성질: (A * B) = GCD(A, B) * LCM(A, B)
# 따라서 LCM = (A * B) // GCD(A, B)
# A와 B의 곱이 크더라도 파이썬에서는 오버플로우 걱정 없이 계산 가능
print((a * b) // gcd(a, b))