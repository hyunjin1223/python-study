# problem: 1764
# tier: silver
import sys

# 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M 입력 (최대 500,000)
# 교집합을 찾아야 하므로 집합(set) 자료형을 사용하는 것이 효율적임
input = sys.stdin.readline

n, m = map(int, input().split())

# 듣도 못한 사람을 set에 저장
unheard = set()
for _ in range(n):
    unheard.add(input().strip())

# 보도 못한 사람을 set에 저장
unseen = set()
for _ in range(m):
    unseen.add(input().strip())

# 두 집합의 교집합(& 연산자)을 구하여 듣지도 보지도 못한 사람 추출
# set의 교집합 연산은 평균적으로 O(min(len(unheard), len(unseen)))의 시간 복잡도를 가짐
result = list(unheard & unseen)

# 사전 순으로 정렬
result.sort()

# 결과 출력: 명단 수와 이름들
print(len(result))
for name in result:
    print(name)