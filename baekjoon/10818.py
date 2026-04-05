# problem: 10818
# tier: bronze

# 정수 개수 입력
N = int(input())

# 정수 리스트 입력 및 변환
arr = list(map(int, input().split()))

# 최솟값과 최댓값 계산 및 출력
print(min(arr), max(arr))