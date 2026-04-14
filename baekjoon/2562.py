# problem: 2562
# tier: bronze

# 9개의 자연수 입력받아 리스트에 저장
arr = []
for i in range(9):
    num = int(input())
    arr.append(num)

# 최댓값과 해당 인덱스 초기화
max_val = arr[0]
max_idx = 0

# 반복문을 통해 최댓값과 그 위치 탐색
for i in range(9):
    if arr[i] > max_val:
        max_val = arr[i]
        max_idx = i

# 최댓값 출력
print(max_val)
# 1번째부터 시작하는 위치(index + 1) 출력
print(max_idx + 1)