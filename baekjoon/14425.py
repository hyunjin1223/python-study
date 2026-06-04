# problem: 14425
# tier: silver
import sys

# N: 집합 S에 포함된 문자열 개수, M: 검사해야 할 문자열 개수
# 문자열의 개수가 많으므로 집합(set)을 사용하여 탐색 속도를 O(1)로 최적화
input = sys.stdin.readline

n, m = map(int, input().split())

# 집합 S에 포함된 문자열들을 set에 저장
s = set()
for _ in range(n):
    s.add(input().strip())

count = 0
# M개의 문자열을 하나씩 확인하며 집합 S에 존재하는지 체크
for _ in range(m):
    check_str = input().strip()
    if check_str in s:
        count += 1

# 포함된 문자열의 총 개수 출력
print(count)