# problem: 11651
# tier: silver
import sys

# 빠른 입력
input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
    # 좌표 저장
    points.append(list(map(int, input().split())))

# y 기준, 같으면 x 기준으로 정렬
points.sort(key=lambda x: (x[1], x[0]))

# 출력
for p in points:
    print(p[0], p[1])