# problem: 18870
# tier: silver
import sys

input = sys.stdin.readline

n = int(input())
coords = list(map(int, input().split()))

# 중복을 제거하고 정렬하여 좌표의 순위를 정함
sorted_coords = sorted(set(coords))

# 각 좌표를 자신의 순위로 매핑
coord_dict = {value: i for i, value in enumerate(sorted_coords)}

# 원래 좌표를 압축된 순위로 변환
print(*(coord_dict[x] for x in coords))