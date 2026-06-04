# problem: 24416
# tier: bronze
import sys

# 알고리즘 수업 - 피보나치 수 1
# 재귀 호출을 이용한 피보나치와 동적 계획법(DP)을 이용한 피보나치의 실행 횟수 비교

def fib(n):
    # 재귀 호출 방식
    # f(1) = 1, f(2) = 1이 리턴되는 횟수가 곧 피보나치 수의 값과 동일함
    # 따라서 별도의 카운트 변수 없이 피보나치 결과값 자체가 실행 횟수가 됨
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    # 동적 계획법(DP) 방식
    # f[3]부터 f[n]까지 루프를 돌며 계산하므로
    # 실행 횟수는 항상 n - 2번이 됨
    count = 0
    f = [0] * (n + 1)
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        count += 1
        f[i] = f[i - 1] + f[i - 2]
    return count

n = int(sys.stdin.readline())

# 1. 재귀 호출의 실행 횟수는 피보나치 수 f(n)과 같음
# 2. DP 방식의 실행 횟수는 n - 2
print(f"{fib(n)} {fibonacci(n)}")