# problem: 2750
# tier: bronze

# 수의 개수 N 입력
n = int(input())
numbers = []

# N개의 수를 입력받아 리스트에 저장
for _ in range(n):
    numbers.append(int(input()))

# 파이썬 내장 정렬 함수(Timsort)를 사용하여 오름차순 정렬
# 중복되지 않는 수들이므로 별도의 처리는 필요 없음
numbers.sort()

# 정렬된 결과를 한 줄씩 출력
for num in numbers:
    print(num)