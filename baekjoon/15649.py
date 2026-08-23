# problem: 15649
# tier: silver
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 현재 만들고 있는 수열
s = []

# 같은 숫자를 다시 선택하지 않도록 방문 여부를 저장
visited = [False] * (n + 1)


def dfs():
    # M개를 모두 선택하면 하나의 수열 완성
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # 1부터 N까지 아직 선택하지 않은 숫자를 확인
    for i in range(1, n + 1):
        if not visited[i]:
            # 숫자를 선택하고 다음 자리로 이동
            visited[i] = True
            s.append(i)

            dfs()

            # 이전 선택을 취소하고 다른 숫자를 선택
            s.pop()
            visited[i] = False


dfs()