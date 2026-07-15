# problem: 11650
# tier: silver
import sys

# 빠른 입력
input = sys.stdin.readline

n = int(input())
points = []

# 좌표 입력
for _ in range(n):
    points.append(tuple(map(int, input().split())))

# x좌표, 같으면 y좌표 기준으로 정렬
points.sort()

# 결과 출력
for p in points:
    print(p[0], p[1]) 