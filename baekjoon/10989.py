# problem: 10989
# tier: bronze
import sys

# 입력 데이터가 최대 10,000,000개로 매우 많지만, 수의 범위는 10,000 이하로 작음
# 메모리 제한이 8MB로 매우 타이트하므로, 모든 수를 리스트에 저장하면 메모리 초과 발생
# 따라서 도수 정렬(Counting Sort)의 원리를 사용하여 메모리를 절약함

input = sys.stdin.readline

n = int(input())

# 인덱스 0부터 10000까지의 카운팅 리스트 생성 (메모리 고정 사용)
# 10001개의 0이 담긴 리스트는 약 40KB 정도로 메모리 제한 내에 충분히 들어옴
count_list = [0] * 10001

# 숫자를 입력받을 때마다 해당 숫자를 인덱스로 하는 카운트를 1 증가
for _ in range(n):
    num = int(input())
    count_list[num] += 1

# 1부터 10000까지 카운트가 0보다 큰 경우에만 그 횟수만큼 출력
for i in range(1, 10001):
    if count_list[i] != 0:
        for _ in range(count_list[i]):
            sys.stdout.write(str(i) + '\n')