# problem: 2805
# tier: silver
import sys

# 빠른 입력
input = sys.stdin.readline

# 나무 수, 필요한 나무 길이
n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 이진 탐색 범위
start = 0
end = max(trees)

result = 0

while start <= end:
    # 현재 절단기 높이
    mid = (start + end) // 2
    total = 0

    # 잘라서 얻는 나무 길이 계산
    for tree in trees:
        if tree > mid:
            total += tree - mid

    # 나무가 충분하면 절단기 높이를 더 높임
    if total >= m:
        result = mid
        start = mid + 1
    # 부족하면 절단기 높이를 낮춤
    else:
        end = mid - 1

# 가능한 최대 높이 출력
print(result)