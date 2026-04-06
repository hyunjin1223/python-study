# problem: 10950
# tier: bronze

# 테스트 케이스 개수 입력
T = int(input())

# T번만큼 반복 수행
for _ in range(T):
    # 두 정수 입력 및 합계 출력
    A, B = map(int, input().split())
    print(A + B)