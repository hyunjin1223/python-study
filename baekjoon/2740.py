# problem: 2740
# tier: silver
import sys

input = sys.stdin.readline

# 행렬 A의 크기와 값 입력
n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]

# 행렬 B의 크기와 값 입력
m, k = map(int, input().split())
matrix_b = [list(map(int, input().split())) for _ in range(m)]

# 결과 행렬은 N x K 크기로 생성
result = [[0] * k for _ in range(n)]

# A의 행과 B의 열을 곱해 결과 행렬을 계산
for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += matrix_a[i][l] * matrix_b[l][j]

# 결과 출력
for row in result:
    print(*row)