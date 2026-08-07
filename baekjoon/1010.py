# problem: 1010
# tier: silver
import sys

# 다리 놓기 문제

# 빠른 입력
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())


# 팩토리얼 계산
def factorial(num):
    res = 1

    for i in range(2, num + 1):
        res *= i

    return res


for _ in range(t):
    n, m = map(int, input().split())

    # 동쪽 M개 중 N개 선택
    bridge_cases = factorial(m) // (
        factorial(n) * factorial(m - n)
    )

    # 가능한 다리 개수 출력
    print(bridge_cases)