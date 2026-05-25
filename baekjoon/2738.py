# problem: 2738
# tier: bronze

# 행렬의 크기 N, M 입력
N, M = map(int, input().split())

# 첫 번째 행렬 A 입력
matrix_A = []
for _ in range(N):
    matrix_A.append(list(map(int, input().split())))

# 두 번째 행렬 B 입력 및 바로 더하기
matrix_B = []
for i in range(N):
    row_B = list(map(int, input().split()))
    # 같은 위치의 원소끼리 더해서 출력
    for j in range(M):
        matrix_A[i][j] += row_B[j]

# 결과 출력
for row in matrix_A:
    print(*row)