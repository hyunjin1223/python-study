# problem: 15552
# tier: bronze

import sys

# 테스트 케이스 개수 T 입력 (빠른 입력 처리)
T = int(sys.stdin.readline())

# T번 반복하며 각 두 수의 합 출력
for _ in range(T):
    # sys.stdin.readline()을 사용하여 빠른 속도로 입력 받음
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)