# problem: 15652
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

    # 현재 숫자부터 선택해 비내림차순을 유지
    for i in range(start, n + 1):
        s.append(i)

        # 같은 숫자를 다시 선택할 수 있도록 i부터 탐색
        dfs(i)

        # 선택을 취소하고 다음 숫자를 확인
        s.pop()


dfs(1)