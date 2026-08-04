# problem: 1904
# tier: silver
import sys

# 01 타일 문제

# 타일 길이 입력
n = int(sys.stdin.readline())

def solve(n):
    # 길이가 1, 2인 경우
    if n == 1:
        return 1
    if n == 2:
        return 2

    # f(1)=1, f(2)=2
    prev2 = 1
    prev1 = 2

    # 이전 두 값을 이용해 현재 값 계산
    for _ in range(3, n + 1):
        current = (prev1 + prev2) % 15746

        # 다음 계산을 위해 값 갱신
        prev2 = prev1
        prev1 = current

    return prev1

# 결과 출력
print(solve(n))