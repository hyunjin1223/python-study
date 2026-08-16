# problem: 2108
# tier: silver
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

# 모든 수의 합을 구해 산술평균 계산
print(round(sum(numbers) / n))

# 오름차순 정렬 후 가운데 값을 중앙값으로 사용
numbers.sort()
print(numbers[n // 2])

# 숫자별 등장 횟수를 세어 최빈값을 찾음
counts = Counter(numbers).most_common()

# 최빈값이 여러 개면 두 번째로 작은 값을 출력
if len(counts) > 1 and counts[0][1] == counts[1][1]:
    max_freq = counts[0][1]
    candidates = [num for num, freq in counts if freq == max_freq]
    
    # 같은 빈도의 숫자들을 오름차순으로 정렬
    candidates.sort()
    print(candidates[1])
else:
    # 최빈값이 하나라면 해당 숫자를 출력
    print(counts[0][0])

# 최댓값과 최솟값의 차이를 계산
print(numbers[-1] - numbers[0])