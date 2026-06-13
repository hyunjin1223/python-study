# problem: 1018
# tier: silver

n, m = map(int, input().split())
board = [input() for _ in range(n)]
repair_counts = []

# 8x8 크기로 자를 수 있는 모든 시작 지점 탐색
for i in range(n - 7):
    for j in range(m - 7):
        draw1 = 0 # 'W'로 시작하는 경우 다시 칠해야 할 개수
        draw2 = 0 # 'B'로 시작하는 경우 다시 칠해야 할 개수

        # 시작 지점 (i, j)부터 8x8 영역 검사
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # 행과 열의 인덱스 합이 짝수/홀수임에 따라 색이 번갈아 나와야 함
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
                else:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
        
        # 두 경우 중 최소값을 리스트에 저장
        repair_counts.append(draw1)
        repair_counts.append(draw2)

# 모든 8x8 경우 중 가장 적게 다시 칠하는 횟수 출력
print(min(repair_counts))