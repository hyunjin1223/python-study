# problem: 1992
# tier: silver
import sys

# 쿼드트리: 같은 색으로 이루어진 영역을 하나의 숫자로 압축하는 문제
input = sys.stdin.readline

n = int(input())
video = [list(input().strip()) for _ in range(n)]


def compress(x, y, size):
    # 현재 영역의 첫 번째 색을 기준으로 확인
    color = video[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != color:
                # 색이 다르면 영역을 4등분해서 다시 확인
                print("(", end="")
                new_size = size // 2

                compress(x, y, new_size)                         # 왼쪽 위
                compress(x, y + new_size, new_size)              # 오른쪽 위
                compress(x + new_size, y, new_size)              # 왼쪽 아래
                compress(x + new_size, y + new_size, new_size)   # 오른쪽 아래

                print(")", end="")
                return

    # 영역 전체가 같은 색이면 해당 색만 출력
    print(color, end="")


compress(0, 0, n)
print()