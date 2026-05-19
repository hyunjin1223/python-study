# problem: 9063
# tier: bronze

n = int(input())
x_list = []
y_list = []

for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

# 모든 점을 포함하는 가장 작은 직사각형의 넓이
# (x의 최댓값 - x의 최솟값) * (y의 최댓값 - y의 최솟값)
width = max(x_list) - min(x_list)
height = max(y_list) - min(y_list)

print(width * height)