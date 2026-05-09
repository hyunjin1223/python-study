# problem: 24266
# tier: bronze

# MenOfPassion(A, n) {
#     sum <- 0;
#     for i from 1 to n
#         for j from 1 to n
#             for k from 1 to n
#                 sum <- sum + A[i] * A[j] * A[k]; # 코드1
#     return sum;
# }

n = int(input())

# 3중 중첩 반복문으로 n * n * n번 실행됨
print(n * n * n)
# n^3 이므로 최고차항의 차수는 3 (O(n^3))
print(3)