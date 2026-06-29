# problem: 1934
# tier: bronze
import sys

# 테스트 케이스의 개수 T 입력
input = sys.stdin.readline
t = int(input())

# 최대공약수(GCD)를 구하는 함수 (유클리드 호제법)
def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수(LCM)는 (a * b) / GCD(a, b) 공식으로 구할 수 있음
for _ in range(t):
    a, b = map(int, input().split())
    
    # 두 수의 곱을 최대공약수로 나누어 최소공배수 산출
    # 결과가 항상 정수이므로 // 연산자 사용
    lcm = (a * b) // get_gcd(a, b)
    print(lcm)