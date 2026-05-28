# problem: 2587
# tier: bronze

numbers = []

# 다섯 개의 자연수를 입력받아 리스트에 저장
for _ in range(5):
    numbers.append(int(input()))

# 평균 계산: 모든 수의 합을 개수(5)로 나눔
avg = sum(numbers) // 5

# 중앙값 계산: 오름차순 정렬 후 가운데(인덱스 2) 위치한 값
numbers.sort()
median = numbers[2]

# 평균과 중앙값을 각각 출력
print(avg)
print(median)