# problem: 2630
# tier: silver
import sys

# 색종이 만들기: 전체 종이가 모두 같은 색이 아니라면 4등분하여 다시 확인하는 분할 정복 문제.
# 하얀색(0), 파란색(1)의 개수를 각각 구해야 함.

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def solve(x, y, size):
    global white, blue
    color = paper[x][y]
    
    # 현재 영역이 모두 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                # 색이 다르면 4등분 (Divide)
                new_size = size // 2
                solve(x, y, new_size)                         # 1사분면 (좌상)
                solve(x, y + new_size, new_size)              # 2사분면 (우상)
                solve(x + new_size, y, new_size)              # 3사분면 (좌하)
                solve(x + new_size, y + new_size, new_size)   # 4사분면 (우하)
                return

    # 모두 같은 색이라면 해당 색상 카운트 증가 (Conquer)
    if color == 0:
        white += 1
    else:
        blue += 1

solve(0, 0, n)
print(white)
print(blue)