# problem: 1541
# tier: silver
import sys

# 잃어버린 괄호 문제

# '-'를 기준으로 식 분리
expression = sys.stdin.readline().strip().split('-')

results = []

for part in expression:
    # 각 묶음의 '+' 값들을 모두 더함
    sub_sum = sum(map(int, part.split('+')))
    results.append(sub_sum)

# 첫 번째 묶음은 더하고
answer = results[0]

# 나머지 묶음은 모두 빼기
for i in range(1, len(results)):
    answer -= results[i]

# 최소값 출력
print(answer)