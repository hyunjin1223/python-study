# problem: 1932
# tier: silver
import sys

# 정수 삼각형 문제

# 빠른 입력
input = sys.stdin.readline

# 삼각형 높이
n = int(input())

# 삼각형 입력
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# 각 위치까지의 최대 합 계산
for i in range(1, n):
    for j in range(len(triangle[i])):
        # 왼쪽 끝은 바로 위에서만 내려올 수 있음
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]

        # 오른쪽 끝은 왼쪽 위에서만 내려올 수 있음
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]

        # 가운데는 두 경로 중 큰 값 선택
        else:
            triangle[i][j] += max(
                triangle[i - 1][j - 1],
                triangle[i - 1][j]
            )

# 마지막 줄에서 최대값 출력
print(max(triangle[n - 1]))