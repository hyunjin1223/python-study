# problem: 2438
# tier: bronze

# 별의 개수(N) 입력
N = int(input())

# 1부터 N까지 반복하며 별 출력
for i in range(1, N + 1):
    # 각 줄마다 i개의 별 출력
    print("*" * i)