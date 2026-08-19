# problem: 10816
# tier: silver
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

# 숫자 카드들을 정렬해서 이분 탐색에 사용할 준비
n = int(input())
cards = sorted(map(int, input().split()))

m = int(input())
queries = list(map(int, input().split()))


def count_by_range(array, value):
    # value가 처음 나오는 위치와 마지막 다음 위치를 구함
    left = bisect_left(array, value)
    right = bisect_right(array, value)

    # 두 위치의 차이가 value의 등장 횟수
    return right - left


result = []

for q in queries:
    result.append(count_by_range(cards, q))

print(*result)