# problem: 2751
# tier: silver
import sys

# 입력 속도 향상을 위해 sys.stdin.readline 사용
# 데이터의 개수가 최대 1,000,000개이므로 input()은 시간 초과 가능성이 높음
input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

# 파이썬의 기본 정렬 알고리즘(Timsort)은 O(N log N)을 보장함
# 문제의 시간 제한 내에 효율적으로 정렬 가능
numbers.sort()

# 출력 속도 향상을 위해 한 번에 합쳐서 출력하거나 sys.stdout.write 사용 가능
# 여기서는 가장 대중적인 join 방식을 사용
print('\n'.join(map(str, numbers)))