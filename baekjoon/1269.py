# problem: 1269
# tier: silver
import sys

# 집합 A와 B의 원소 개수 입력
input = sys.stdin.readline
n, m = map(int, input().split())

# 대칭 차집합은 (A-B)와 (B-A)의 합집합임
# 파이썬의 set 자료형은 차집합(-)과 합집합(|) 연산을 효율적으로 지원함

# 집합 A 입력
set_a = set(map(int, input().split()))
# 집합 B 입력
set_b = set(map(int, input().split()))

# 방법 1: 직접 정의대로 계산
# (set_a - set_b) | (set_b - set_a)

# 방법 2: 대칭 차집합 연산자(^) 사용
# 두 집합의 합집합에서 교집합을 뺀 것과 동일한 결과
symmetric_diff = set_a ^ set_b

# 대칭 차집합의 원소 개수 출력
print(len(symmetric_diff))