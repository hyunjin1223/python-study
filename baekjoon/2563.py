# problem: 2563
# tier: silver

# 색종이의 개수 입력
N = int(input())

# 100x100 크기의 도화지 초기화 (0: 빈 공간, 1: 색종이가 붙은 공간)
canvas = [[0] * 100 for _ in range(100)]

for _ in range(N):
    # 색종이의 왼쪽 아래 모서리 좌표 입력
    x, y = map(int, input().split())
    
    # 10x10 크기만큼 도화지에 표시
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1

# 도화지에서 1의 개수(색종이가 붙은 면적) 합산
total_area = 0
for row in canvas:
    total_area += sum(row)

print(total_area)