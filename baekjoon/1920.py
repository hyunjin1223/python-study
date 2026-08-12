# problem: 1920
# tier: silver
import sys

# 수 찾기 문제

# 빠른 입력
input = sys.stdin.readline

n = int(input())

# 이분 탐색을 위해 정렬
a = sorted(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))


def binary_search(target):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        # 값을 찾은 경우
        if a[mid] == target:
            return 1

        # 오른쪽 탐색
        if a[mid] < target:
            low = mid + 1

        # 왼쪽 탐색
        else:
            high = mid - 1

    # 값이 없는 경우
    return 0


# 각 숫자의 존재 여부 출력
for t in targets:
    print(binary_search(t))