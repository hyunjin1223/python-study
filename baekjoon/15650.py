# problem: 15650
# tier: silver
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 현재 만들고 있는 조합
s = []


def dfs(start):
    # M개를 선택하면 하나의 조합 완성
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # start부터 선택해서 항상 오름차순을 유지
    for i in range(start, n + 1):
        s.append(i)

        # 다음 숫자는 현재 숫자보다 큰 값에서 선택
        dfs(i + 1)

        # 선택을 취소하고 다음 숫자를 확인
        s.pop()


dfs(1)