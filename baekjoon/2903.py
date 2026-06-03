# problem: 2903
# tier: bronze

N = int(input())

# 한 변의 점 개수: 2^N + 1
# 전체 점 개수: (한 변의 점 개수)^2
print((2**N + 1)**2)