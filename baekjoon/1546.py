# problem: 1546
# tier: bronze

# 과목 수 N 입력
N = int(input())

# 점수 리스트 입력
arr = list(map(int, input().split()))

# 최고 점수 M 찾기
M = max(arr)

# 새로운 점수 합계 계산
sum_score = 0
for i in arr:
    sum_score += i / M * 100

# 새로운 평균 출력
print(sum_score / N)