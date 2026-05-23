# problem: 3009
# tier: bronze

x_coords = []
y_coords = []

# 세 점의 좌표 입력
for _ in range(3):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)

# 직사각형이 되려면 각 좌표값이 두 번씩 나타나야 함
# 하나만 존재하는 좌표를 찾아서 네 번째 점 완성
res_x = 0
res_y = 0

for i in range(3):
    if x_coords.count(x_coords[i]) == 1:
        res_x = x_coords[i]
    if y_coords.count(y_coords[i]) == 1:
        res_y = y_coords[i]

print(res_x, res_y)