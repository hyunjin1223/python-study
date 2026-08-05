# problem: 1780
# tier: silver
import sys

# 종이의 개수 문제

# 빠른 입력
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# -1, 0, 1 종이 개수 저장
result = [0, 0, 0]

def solve(x, y, size):
    # 현재 영역의 기준 값
    current_val = paper[x][y]

    # 현재 영역이 모두 같은 값인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != current_val:
                # 값이 다르면 9등분
                new_size = size // 3

                for row in range(3):
                    for col in range(3):
                        solve(
                            x + row * new_size,
                            y + col * new_size,
                            new_size
                        )
                return

    # 모두 같은 값이면 해당 개수 증가
    result[current_val + 1] += 1

# 전체 종이 검사
solve(0, 0, n)

# 결과 출력
for count in result:
    print(count)