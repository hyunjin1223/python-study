# problem: 4134
# tier: silver
import sys

# 소수 판별 함수
def is_prime(x):
    # 2보다 작은 수는 소수가 아님
    if x < 2:
        return False

    # 제곱근까지만 나누어 확인
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True

# 빠른 입력
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    n = int(input())

    # n 이상인 가장 작은 소수 찾기
    while True:
        if is_prime(n):
            print(n)
            break

        # 소수가 아니면 다음 수 확인
        n += 1