# problem: 15651
# tier: silver
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 현재 만들고 있는 수열
s = []


def dfs():
    # M개를 선택하면 하나의 수열 완성
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # 중복 선택이 가능하므로 항상 1부터 N까지 확인
    for i in range(1, n + 1):
        s.append(i)

        # 다음 숫자를 선택
        dfs()

        # 선택을 취소하고 다음 숫자를 확인
        s.pop()


dfs()