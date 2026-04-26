# problem: 1085
# tier: bronze

x, y, w, h = map(int, input().split())

# 각 경계선까지의 거리 계산:
# x (왼쪽), y (아래), w-x (오른쪽), h-y (위)
# 이 중 최솟값이 가장 가까운 거리
print(min(x, y, w - x, h - y))