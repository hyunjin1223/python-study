# problem: 2485
# tier: silver
import sys

# 최대공약수(GCD)를 구하는 유클리드 호제법 함수
def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 이미 심어져 있는 가로수의 수 N 입력
input = sys.stdin.readline
n = int(input())

# 가로수의 위치를 저장할 리스트
trees = []
for _ in range(n):
    trees.append(int(input()))

# 1. 가로수 사이의 간격들을 구함
# 예: [1, 3, 7, 13] -> 간격: [2, 4, 6]
intervals = []
for i in range(n - 1):
    intervals.append(trees[i+1] - trees[i])

# 2. 모든 간격들의 최대공약수(GCD)를 구함
# 이 GCD가 가로수 사이의 가능한 최대 일정한 간격이 됨
g = intervals[0]
for j in range(1, len(intervals)):
    g = get_gcd(g, intervals[j])

# 3. 추가로 심어야 하는 가로수의 개수 계산
# (전체 거리 // 간격) - (이미 있는 가로수 개수 - 1)
# 각 간격에 대해 (간격 // GCD - 1)을 모두 더하는 방식과 동일
count = 0
for dist in intervals:
    count += (dist // g) - 1

print(count)